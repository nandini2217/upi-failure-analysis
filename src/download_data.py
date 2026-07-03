"""
Data Acquisition Script
------------------------
This project uses the "Product Wise Declined (Business/Technical) Transactions"
dataset published by NPCI, hosted on India Data Portal (free, no login required).

Source: https://ckandev.indiadataportal.com/dataset/national-payments-corporation-of-india-npci/resource/f8c33592-34cd-4bdf-b4b8-d845d67b4eb4
Original NPCI source: https://www.npci.org.in/statistics/bd-td-and-uptime

Direct CSV download:
https://ckandev.indiadataportal.com/datastore/dump/f8c33592-34cd-4bdf-b4b8-d845d67b4eb4?bom=True

Coverage: 107 issuer banks, monthly, 2021-2023
Columns: date, product, issuer_bank, total_volume, 
         approved_transaction_volume, business_decline_transactions, 
         technical_decline_transactions

Steps:
    1. Visit the direct CSV download link above (or run this script with 
       requests installed to fetch it automatically)
    2. Save as: data/raw/upi_declined_transactions.csv
"""

import os
import urllib.request

RAW_DATA_PATH = "data/raw/upi_declined_transactions.csv"
SOURCE_URL = "https://ckandev.indiadataportal.com/datastore/dump/f8c33592-34cd-4bdf-b4b8-d845d67b4eb4?bom=True"

def download_data():
    os.makedirs("data/raw", exist_ok=True)
    if os.path.exists(RAW_DATA_PATH):
        print(f"Data already exists at {RAW_DATA_PATH}")
        return
    print("Downloading UPI declined transactions dataset...")
    urllib.request.urlretrieve(SOURCE_URL, RAW_DATA_PATH)
    print(f"Saved to {RAW_DATA_PATH}")

if __name__ == "__main__":
    download_data()