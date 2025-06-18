"""Constantes pour le gestionnaire de stock de piles."""

DOMAIN = "pile_stock_manager"
CONF_STOCK_PATH = "stock_path"

# Types de piles supportées (NOMS CORRIGÉS)
PILE_TYPES = [
    "CR2450",
    "CR2032",
    "CR2025",
    "CR1620",
    "CR2016",
    "LR44",
    "AA",        # Changé de "Type AA" à "AA"
    "AAA"        # Changé de "Type AAA" à "AAA"
]

# Services
SERVICE_ADD_STOCK = "add_stock"
SERVICE_REMOVE_STOCK = "remove_stock"
SERVICE_RESET_STOCK = "reset_stock"

# Attributs par défaut
DEFAULT_STOCK_PATH = "pile_stock.json"
DEFAULT_ALERT_THRESHOLD = 3
