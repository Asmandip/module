import asyncio
from flask import Flask, render_template, request, jsonify
from dashboard_config import DashboardConfig
from bitget_api import BitgetAPI
from dotenv import load_dotenv
import os

load_dotenv()  # .env ফাইল লোড করুন

app = Flask(__name__)
config_manager = DashboardConfig()
bitget_api = BitgetAPI()

@app.route('/')
def dashboard():
    config = config_manager.get_config()
    return render_template('dashboard.html', config=config)

@app.route('/update-config', methods=['POST'])
def update_config():
    data = request.json
    for key, value in data.items():
        config_manager.update_setting(key, value)
    return jsonify({"status": "success"})

@app.route('/get-balance')
def get_balance():
    if config_manager.config['api_enabled']:
        balance = bitget_api.get_account_balance()
        return jsonify(balance)
    return jsonify({"error": "API disabled"})

# অন্যান্য রাউট এখানে অ্যাড করুন

if __name__ == '__main__':
    app.run(debug=True)