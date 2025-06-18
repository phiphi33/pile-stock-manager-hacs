"""Gestionnaire de Stock de Piles pour Home Assistant."""
import logging
import json
import os
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers import config_validation as cv
import voluptuous as vol

from .const import DOMAIN, PILE_TYPES, SERVICE_ADD_STOCK, SERVICE_REMOVE_STOCK, SERVICE_RESET_STOCK

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["sensor"]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Configuration de l'intégration."""
    
    # Initialiser le stockage des données
    hass.data.setdefault(DOMAIN, {})
    
    # Charger les données de stock
    stock_data = await hass.async_add_executor_job(_load_stock_data, hass)
    hass.data[DOMAIN]["stock"] = stock_data
    
    # Configurer les plateformes
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    
    # Enregistrer les services
    await _register_services(hass)
    
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Déchargement de l'intégration."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    
    if unload_ok:
        hass.data[DOMAIN].pop("stock", None)
    
    return unload_ok

def _load_stock_data(hass: HomeAssistant) -> dict:
    """Charger les données de stock depuis le fichier JSON."""
    stock_file = os.path.join(hass.config.config_dir, "pile_stock.json")
    
    if os.path.exists(stock_file):
        try:
            with open(stock_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            _LOGGER.error("Erreur lors du chargement du stock: %s", e)
    
    # Données par défaut
    return {pile_type: 0 for pile_type in PILE_TYPES}

def _save_stock_data(hass: HomeAssistant, stock_data: dict):
    """Sauvegarder les données de stock dans le fichier JSON."""
    stock_file = os.path.join(hass.config.config_dir, "pile_stock.json")
    
    try:
        with open(stock_file, 'w') as f:
            json.dump(stock_data, f, indent=2)
    except Exception as e:
        _LOGGER.error("Erreur lors de la sauvegarde du stock: %s", e)

async def _force_update_sensors(hass: HomeAssistant):
    """Forcer la mise à jour de tous les capteurs de stock."""
    entities_to_update = [
        "sensor.stock_cr2450",
        "sensor.stock_cr2032", 
        "sensor.stock_cr2025",
        "sensor.stock_cr1620",
        "sensor.stock_cr2016",
        "sensor.stock_lr44",
        "sensor.stock_aa",        # CORRIGÉ : était stock_type_aa
        "sensor.stock_aaa",       # CORRIGÉ : était stock_type_aaa
        "sensor.stock_total_piles"
    ]
    
    _LOGGER.debug("Forçage de la mise à jour des capteurs de stock")
    
    try:
        await hass.services.async_call(
            "homeassistant",
            "update_entity",
            {"entity_id": entities_to_update}
        )
        _LOGGER.debug("Mise à jour forcée des capteurs de stock réussie")
    except Exception as e:
        _LOGGER.error("Erreur lors de la mise à jour forcée des capteurs: %s", e)

async def _register_services(hass: HomeAssistant):
    """Enregistrer les services personnalisés."""
    
    async def add_stock(call):
        """Service pour ajouter du stock."""
        pile_type = call.data.get("pile_type")
        quantity = call.data.get("quantity", 1)
        
        if pile_type in hass.data[DOMAIN]["stock"]:
            # Modifier le stock en mémoire
            hass.data[DOMAIN]["stock"][pile_type] += quantity
            
            # Sauvegarder sur disque
            await hass.async_add_executor_job(_save_stock_data, hass, hass.data[DOMAIN]["stock"])
            
            # FORCER la mise à jour des capteurs
            await _force_update_sensors(hass)
            
            _LOGGER.info("Ajouté %d %s au stock (nouveau total: %d)", 
                        quantity, pile_type, hass.data[DOMAIN]["stock"][pile_type])
    
    async def remove_stock(call):
        """Service pour retirer du stock."""
        pile_type = call.data.get("pile_type")
        quantity = call.data.get("quantity", 1)
        
        if pile_type in hass.data[DOMAIN]["stock"]:
            current = hass.data[DOMAIN]["stock"][pile_type]
            new_value = max(0, current - quantity)
            
            # Modifier le stock en mémoire
            hass.data[DOMAIN]["stock"][pile_type] = new_value
            
            # Sauvegarder sur disque
            await hass.async_add_executor_job(_save_stock_data, hass, hass.data[DOMAIN]["stock"])
            
            # FORCER la mise à jour des capteurs
            await _force_update_sensors(hass)
            
            _LOGGER.info("Retiré %d %s du stock (nouveau total: %d)", 
                        quantity, pile_type, new_value)
    
    async def reset_stock(call):
        """Service pour remettre à zéro tout le stock."""
        _LOGGER.warning("RAZ du stock demandée - Remise à zéro de tous les types de piles")
        
        # Remettre tous les stocks à zéro
        for pile_type in hass.data[DOMAIN]["stock"]:
            hass.data[DOMAIN]["stock"][pile_type] = 0
        
        # Sauvegarder les modifications
        await hass.async_add_executor_job(_save_stock_data, hass, hass.data[DOMAIN]["stock"])
        
        # FORCER la mise à jour des capteurs
        await _force_update_sensors(hass)
        
        _LOGGER.info("✅ Stock complet remis à zéro - Tous les types de piles: 0")
    
    # Schémas des services
    add_stock_schema = vol.Schema({
        vol.Required("pile_type"): vol.In(PILE_TYPES),
        vol.Optional("quantity", default=1): cv.positive_int,
    })
    
    remove_stock_schema = vol.Schema({
        vol.Required("pile_type"): vol.In(PILE_TYPES),
        vol.Optional("quantity", default=1): cv.positive_int,
    })
    
    reset_stock_schema = vol.Schema({})  # Pas de paramètres requis pour RAZ
    
    # Enregistrement des services
    hass.services.async_register(DOMAIN, SERVICE_ADD_STOCK, add_stock, schema=add_stock_schema)
    hass.services.async_register(DOMAIN, SERVICE_REMOVE_STOCK, remove_stock, schema=remove_stock_schema)
    hass.services.async_register(DOMAIN, SERVICE_RESET_STOCK, reset_stock, schema=reset_stock_schema)
