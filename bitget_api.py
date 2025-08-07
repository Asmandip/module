import hashlib
import hmac
import time
import requests
import json
import os

class BitgetAPI:
    def __init__(self):
        self.base_url = "https://api.bitget.com"
        self.api_key = os.getenv('BITGET_API_KEY')
        self.secret_key = os.getenv('BITGET_SECRET_KEY')
        self.passphrase = os.getenv('BITGET_PASSPHRASE')
        
    def generate_signature(self, method, path, body=None):
        timestamp = str(int(time.time() * 1000))
        message = timestamp + method.upper() + path
        if body:
            message += json.dumps(body, separators=(',', ':'))
        signature = hmac.new(
            self.secret_key.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        return timestamp, signature

    def get_account_balance(self):
        path = "/api/spot/v1/account/assets"
        timestamp, signature = self.generate_signature("GET", path)
        
        headers = {
            "ACCESS-KEY": self.api_key,
            "ACCESS-SIGN": signature,
            "ACCESS-TIMESTAMP": timestamp,
            "ACCESS-PASSPHRASE": self.passphrase,
            "Content-Type": "application/json"
        }
        
        response = requests.get(self.base_url + path, headers=headers)
        return response.json()
    
    # অন্যান্য API মেথড এখানে অ্যাড করুন
