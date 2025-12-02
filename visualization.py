import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. Connect to the Data Warehouse (SQLite)
conn = sqlite3.connect('market_data.db')

# 2. Load data directly into Pandas
# (Pandas can read SQL queries directly! This is a Superpower.)
df = pd.read_sql_query("SELECT * FROM MarketData", conn)

conn.close()

# 3. Fix Data Types
# The database gave us strings, but we need 'datetime' objects for the chart.
df['timestamp'] = pd.to_datetime(df['timestamp'])

# 4. Create the Plot
plt.figure(figsize=(10, 5)) # Set the window size
plt.plot(df['timestamp'], df['price'], marker='o', linestyle='-', color='b')

# 5. Make it pretty
plt.title('Bitcoin Price Trend (Live Pipeline Data)')
plt.xlabel('Time')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.xticks(rotation=45) # Rotate time labels so they don't overlap
plt.tight_layout()

# 6. Show the graph
print("Opening graph...")
plt.show()
