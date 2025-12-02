import requests
import pandas as pd
import datetime
import os
import time
import sqlite3


n = 5
file_exists = os.path.isfile("bitcoin_prices.csv")
while n>0:
    current_time = datetime.datetime.now()
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    data = response.json()
    record = {
        "name":"bitcoin",
        "price":data['bitcoin']['usd'],
        "timestamp":str(current_time)
    }
    df = pd.DataFrame([record])
    file_exists = os.path.isfile("bitcoin_prices.csv")
    df.to_csv("bitcoin_prices.csv", index=False, mode="a", header=not file_exists)
    conn = sqlite3.connect('market_data.db')
    cursor = conn.cursor()
    insert_query = "INSERT INTO MarketData (name, price, timestamp) VALUES (?, ?, ?)"
    cursor.execute(insert_query, (record['name'], record['price'], record['timestamp']))
    conn.commit()
    conn.close()
    n = n-1
    time.sleep(60)
print("Pipeline Finished")
