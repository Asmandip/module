import json
import os
from pathlib import Path

CONFIG_DIR = Path("config")
CONFIG_FILE = CONFIG_DIR / "dashboard_config.json"

class DashboardConfig:
    def __init__(self):
        self.config = self.load_config()
        
    def load_config(self):
        if not CONFIG_FILE.exists():
            CONFIG_DIR.mkdir(exist_ok=True)
            default_config = {
                "api_enabled": True,
                "refresh_interval": 60,
                "default_pair": "BTCUSDT",
                "features": {
                    "auto_trading": False,
                    "withdrawals": False,
                    "alerts": True,
                    "charting": True
                }
            }
            with open(CONFIG_FILE, 'w') as f:
                json.dump(default_config, f, indent=4)
            return default_config
        
        with open(CONFIG_FILE) as f:
            return json.load(f)
            
    def save_config(self):
        with open(CONFIG_FILE, 'w') as f:
            json.dump(self.config, f, indent=4)
            
    def update_setting(self, key, value):
        keys = key.split('.')
        current = self.config
        for k in keys[:-1]:
            current = current.setdefault(k, {})
        current[keys[-1]] = value
        self.save_config()
        
    def get_config(self):
        return self.config
