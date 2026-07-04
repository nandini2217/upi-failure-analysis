"""
Wayback Machine Snapshot Finder
---------------------------------
NPCI's live site blocks automated scraping (robots.txt disallows it).
Instead, we use the Internet Archive's Wayback Machine, which hosts 
historical snapshots of public pages and does not block this kind of 
programmatic access.

This script lists available snapshots of NPCI's UPI Ecosystem Statistics 
page so we know which months/years we can actually pull data from.
"""

import requests

CDX_API = "http://web.archive.org/cdx/search/cdx"
TARGET_URL = "npci.org.in/what-we-do/upi/upi-ecosystem-statistics"

def find_snapshots():
    params = {
        "url": TARGET_URL,
        "output": "json",
        "filter": "statuscode:200",
        "collapse": "timestamp:6",  # one snapshot per month (YYYYMM)
        "limit": 100
    }
    resp = requests.get(CDX_API, params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    if len(data) <= 1:
        print("No snapshots found.")
        return []

    header, rows = data[0], data[1:]
    print(f"Found {len(rows)} snapshots\n")
    snapshots = []
    for row in rows:
        record = dict(zip(header, row))
        timestamp = record["timestamp"]
        wayback_url = f"http://web.archive.org/web/{timestamp}/https://www.{TARGET_URL}"
        snapshots.append(wayback_url)
        print(f"{timestamp[:4]}-{timestamp[4:6]} -> {wayback_url}")

    return snapshots

if __name__ == "__main__":
    find_snapshots()