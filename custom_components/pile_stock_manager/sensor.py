"""Capteurs avec mise à jour forcée pour le gestionnaire de stock de piles."""
import logging
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN, PILE_TYPES

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Configuration des capteurs avec mise à jour forcée."""
    
    entities = []
    
    # Créer un capteur pour chaque type de pile
    for pile_type in PILE_TYPES:
        entities.append(PileStockSensor(hass, pile_type))
    
    # Capteur de stock total
    entities.append(TotalStockSensor(hass))
    
    async_add_entities(entities)

class PileStockSensor(SensorEntity):
    """Capteur pour le stock d'un type de pile avec mise à jour forcée."""
    
    def __init__(self, hass: HomeAssistant, pile_type: str):
        """Initialiser le capteur."""
        self._hass = hass
        self._pile_type = pile_type
        self._attr_name = f"Stock {pile_type}"
        self._attr_unique_id = f"{DOMAIN}_{pile_type.lower().replace(' ', '_')}_stock"
        self._attr_icon = "mdi:battery"
        self._attr_unit_of_measurement = "unités"
        self._attr_force_update = True  # FORCER la mise à jour
        self._attr_should_poll = True   # ACTIVER le polling
    
    @property
    def state(self):
        """Retourner l'état du capteur."""
        return self._hass.data[DOMAIN]["stock"].get(self._pile_type, 0)
    
    async def async_update(self):
        """Mise à jour forcée du capteur."""
        # Relire les données depuis la source
        if DOMAIN in self._hass.data and "stock" in self._hass.data[DOMAIN]:
            self._attr_native_value = self._hass.data[DOMAIN]["stock"].get(self._pile_type, 0)
        
    @property
    def extra_state_attributes(self):
        """Attributs supplémentaires."""
        return {
            "pile_type": self._pile_type,
            "last_updated": "now"
        }

class TotalStockSensor(SensorEntity):
    """Capteur pour le stock total avec mise à jour forcée."""
    
    def __init__(self, hass: HomeAssistant):
        """Initialiser le capteur."""
        self._hass = hass
        self._attr_name = "Stock Total Piles"
        self._attr_unique_id = f"{DOMAIN}_total_stock"
        self._attr_icon = "mdi:package-variant"
        self._attr_unit_of_measurement = "unités"
        self._attr_force_update = True  # FORCER la mise à jour
        self._attr_should_poll = True   # ACTIVER le polling
    
    @property
    def state(self):
        """Retourner l'état du capteur."""
        return sum(self._hass.data[DOMAIN]["stock"].values())
    
    async def async_update(self):
        """Mise à jour forcée du capteur."""
        # Recalculer le total
        if DOMAIN in self._hass.data and "stock" in self._hass.data[DOMAIN]:
            self._attr_native_value = sum(self._hass.data[DOMAIN]["stock"].values())
    
    @property
    def extra_state_attributes(self):
        """Attributs supplémentaires."""
        return self._hass.data[DOMAIN]["stock"]
