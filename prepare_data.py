# Data Aggregator for Product Groups
import os
import pandas as pd
import json

# Relative to script location
script_dir = os.path.dirname(os.path.abspath(__file__))
workspace_dir = os.path.dirname(script_dir)

print("Loading KPI database...")
kpi_df = pd.read_excel(os.path.join(workspace_dir, "RET_KPI_Sales_Database.xlsx"))
kpi_cols = ["Store Name", "Year", "Month", "Traffic", "Transactions", "NS", "NS @FP", "NQ", "NQ @FP", "SM"]
kpi_df[kpi_cols] = kpi_df[kpi_cols].fillna(0)
kpi_data = kpi_df[kpi_cols].values.tolist()

print("Loading Product database...")
prod_df = pd.read_excel(os.path.join(workspace_dir, "RET_Product_Sales_Database.xlsx"))
prod_groupby_cols = ["Store Name", "Category", "Division", "Product Group", "Gender", "Year", "Month"]
prod_sum_cols = ["NS", "NQ", "SM"]

prod_df[prod_sum_cols] = prod_df[prod_sum_cols].fillna(0)
print("Grouping product records by Product Group...")
agg_df = prod_df.groupby(prod_groupby_cols)[prod_sum_cols].sum().reset_index()
prod_cols = prod_groupby_cols + prod_sum_cols
prod_data = agg_df[prod_cols].values.tolist()

output_path = os.path.join(script_dir, "scratch", "data_vars.js")
print(f"Saving variables to: {output_path}")
with open(output_path, "w", encoding="utf-8") as f:
    f.write("// Retail KPI Data Definitions\n")
    f.write(f"const KPI_COLS = {json.dumps(kpi_cols)};\n")
    f.write(f"const KPI_DATA = {json.dumps(kpi_data)};\n")
    f.write(f"const PROD_COLS = {json.dumps(prod_cols)};\n")
    f.write(f"const PROD_DATA = {json.dumps(prod_data)};\n")

print("Successfully regenerated data_vars.js!")
