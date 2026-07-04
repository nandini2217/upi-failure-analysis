"""
Data Exploration Script

Quick profiling of the raw dataset before writing cleaning logic.
Run this first whenever a new raw file is added, to catch schema 
surprises (mixed products, percentage vs absolute values, nulls, 
inconsistent bank naming) before they leak into the cleaning pipeline.
"""

import pandas as pd

RAW_DATA_PATH = "data/raw/npci_declined_transactions.csv"

def explore():
    df = pd.read_csv(RAW_DATA_PATH)

    print("=" * 50)
    print("SHAPE:", df.shape)

    print("\n" + "=" * 50)
    print("UNIQUE PRODUCTS:")
    print(df["product"].unique())

    print("\n" + "=" * 50)
    print("UPI ROW COUNT:", (df["product"] == "UPI").sum())

    print("\n" + "=" * 50)
    print("NULL COUNTS:")
    print(df.isnull().sum())

    print("\n" + "=" * 50)
    print("DATE RANGE:", df["date"].min(), "to", df["date"].max())

    print("\n" + "=" * 50)
    print("UNIQUE BANKS:", df["issuer_bank"].nunique())
    print(df["issuer_bank"].unique()[:15])  # sample


def validate_percentage_columns():
    """
    Confirms whether approved/BD/TD columns are percentages (summing to ~100)
    or raw transaction counts. This determines how we label and interpret 
    these columns in cleaning and analysis.
    """
    df = pd.read_csv(RAW_DATA_PATH)
    df["check_sum"] = (
        df["approved_transaction_volume"]
        + df["business_decline_transactions"]
        + df["technical_decline_transactions"]
    )
    print("=" * 50)
    print("CHECK SUM STATS (approved + BD + TD):")
    print(df["check_sum"].describe())
    print("\nSample rows:")
    print(df[["approved_transaction_volume", "business_decline_transactions",
               "technical_decline_transactions", "check_sum"]].head())
    

if __name__ == "__main__":
    explore()
    validate_percentage_columns()