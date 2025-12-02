# Bitcoin-ETL-Pipeline
# 📈 Live Bitcoin ETL Pipeline

## Project Overview
This project is an end-to-end Data Engineering pipeline that extracts real-time cryptocurrency data, transforms it, and loads it into a data warehouse for analysis.

## 🏗 Architecture
**Source (CoinGecko API)** -> **Python (Extract)** -> **Pandas (Transform)** -> **SQLite (Load)** -> **Matplotlib (Visualize)**

## 🔧 Technologies Used
* **Python:** Main programming language.
* **Pandas:** Data manipulation and cleaning.
* **SQLite:** Relational database for storage.
* **Matplotlib:** Data visualization.
* **Requests:** API data extraction.

## 🚀 How to Run
1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Run the pipeline to start collecting data:
    ```bash
    python etl_pipeline.py
    ```
3.  Visualize the data trend:
    ```bash
    python visualization.py
    ```

## 👨‍💻 Author
[Raghavendra Jinde]
