"""
Quick SQL Query Runner
------------------------
Runs the core business-question queries from sql/queries.sql against 
the SQLite database and prints results.
"""

import sqlite3

DB_PATH = "data/npci.db"

def run_query(query, description=""):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.execute(query)
    print(f"\n--- {description} ---")
    for row in cursor.fetchall():
        print(row)
    conn.close()

if __name__ == "__main__":
    run_query(
        """
        SELECT bank, ROUND(AVG(td_pct), 2) AS avg_td_pct
        FROM declined_transactions
        GROUP BY bank
        ORDER BY avg_td_pct DESC
        LIMIT 10
        """,
        "Q1: Top 10 banks by average TECHNICAL decline rate"
    )

    run_query(
        """
        SELECT bank, ROUND(AVG(bd_pct), 2) AS avg_bd_pct
        FROM declined_transactions
        GROUP BY bank
        ORDER BY avg_bd_pct DESC
        LIMIT 10
        """,
        "Q2: Top 10 banks by average BUSINESS decline rate"
    )

    run_query(
        """
        SELECT product,
               ROUND(AVG(bd_pct), 2) AS avg_bd_pct,
               ROUND(AVG(td_pct), 2) AS avg_td_pct,
               ROUND(AVG(total_decline_pct), 2) AS avg_total_decline_pct
        FROM declined_transactions
        GROUP BY product
        """,
        "Q3: NFS vs AEPS - average decline rates"
    )

    run_query(
        """
        SELECT year, month, ROUND(AVG(total_decline_pct), 2) AS avg_total_decline_pct
        FROM declined_transactions
        GROUP BY year, month
        ORDER BY year, month
        """,
        "Q4: Monthly trend of total decline rate"
    )

    run_query(
        """
        SELECT bank,
               ROUND(AVG(total_volume), 2) AS avg_volume,
               ROUND(AVG(total_decline_pct), 2) AS avg_total_decline_pct
        FROM declined_transactions
        GROUP BY bank
        ORDER BY avg_volume DESC
        LIMIT 15
        """,
        "Q5: Big banks vs small banks - volume vs decline rate"
    )

    run_query(
        """
        SELECT year, month,
               ROUND(AVG(bd_pct), 2) AS avg_bd_pct,
               ROUND(AVG(td_pct), 2) AS avg_td_pct
        FROM declined_transactions
        GROUP BY year, month
        ORDER BY year, month
        """,
        "Q6: BD vs TD trend over time - is TD improving while BD stays flat?"
    )