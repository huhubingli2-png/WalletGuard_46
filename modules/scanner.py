import requests

API_KEY = "Your_BscScan_API_Key"
BSC_SCAN_URL = "https://api.bscscan.com/api"

def scan_wallet(address):
    try:
        params = {
            "module": "account",
            "action": "tokenapproval",
            "address": address,
            "apikey": API_KEY
        }
        response = requests.get(BSC_SCAN_URL, params=params)
        data = response.json()
        if data["status"] == "1":
            return data["result"]
        else:
            return []
    except Exception as e:
        print(f"扫描失败: {e}")
        return []
