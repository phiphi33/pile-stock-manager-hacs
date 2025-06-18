"""Configuration flow pour le gestionnaire de stock de piles."""
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback

from .const import DOMAIN

class PileStockConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Configuration flow."""
    
    VERSION = 1
    
    async def async_step_user(self, user_input=None):
        """Étape de configuration utilisateur."""
        if user_input is not None:
            return self.async_create_entry(
                title="Gestionnaire Stock Piles",
                data=user_input
            )
        
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({})
        )
