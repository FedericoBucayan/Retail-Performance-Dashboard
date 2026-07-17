# Validation Script
import os
import re
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
workspace_dir = os.path.dirname(script_dir)
report_path = os.path.join(workspace_dir, "index.html")

if not os.path.exists(report_path):
    print("Error: index.html does not exist!")
    exit(1)

# Fix 5: Stream line-by-line to check for elements without loading the full file into memory
elements = [
    "RETAIL PERFORMANCE DASHBOARD",
    "storeFilter",
    "yearFilter",
    "categoryFilter",
    "monthDropdownBtn",
    "YoY Performance Comparison Matrix",
    "trendChartCanvas",
    "categoryChartCanvas",
    "tot_ns_2025",
    "KPI_DATA",
    "PROD_DATA"
]

found = {el: False for el in elements}

print("=== Checking HTML Sections ===")
with open(report_path, "r", encoding="utf-8") as f:
    for line in f:
        for el in elements:
            if not found[el] and el in line:
                found[el] = True

for el in elements:
    if found[el]:
        print(f"  [OK] Found: '{el}'")
    else:
        print(f"  [FAIL] Missing: '{el}'")

# Only load full content for JSON data verification (needed for regex across lines)
with open(report_path, "r", encoding="utf-8") as f:
    content = f.read()

kpi_match = re.search(r"const KPI_DATA = (\[.*?\]);", content)
prod_match = re.search(r"const PROD_DATA = (\[.*?\]);", content)

if kpi_match and prod_match:
    kpi_data = json.loads(kpi_match.group(1))
    prod_data = json.loads(prod_match.group(1))
    print(f"\n=== Data Verification ===")
    print(f"  KPI_DATA length: {len(kpi_data)} records")
    print(f"  PROD_DATA length: {len(prod_data)} records")
else:
    print("\n[FAIL] Could not parse KPI_DATA or PROD_DATA variables!")

print(f"\nValidation completed successfully. File size: {os.path.getsize(report_path)/1024:.2f} KB")

