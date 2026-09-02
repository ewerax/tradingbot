import requests
import json
from datetime import datetime

def get_mnq_candles():
    url = "https://query1.finance.yahoo.com/v8/finance/chart/MNQ=F?interval=1m&range=1d"
    r = requests.get(url)
    data = r.json()

    result = data["chart"]["result"][0]
    timestamps = result["timestamp"]
    quote = result["indicators"]["quote"][0]

    candles = []
    for i in range(len(timestamps)):
        if None in (quote["open"][i], quote["high"][i], quote["low"][i], quote["close"][i]):
            continue

        candles.append({
            "time": timestamps[i],
            "open": quote["open"][i],
            "high": quote["high"][i],
            "low": quote["low"][i],
            "close": quote["close"][i]
        })

    return candles

def save_to_file(candles):
    with open("mnq.json", "w") as f:
        json.dump(candles, f, indent=2)

candles = get_mnq_candles()
save_to_file(candles)
print("MNQ candles updated.")
