# Compiler Script for Retail KPI Dashboard
import os
import datetime

script_dir = os.path.dirname(os.path.abspath(__file__))
workspace_dir = os.path.dirname(script_dir)

# Calculate latest modification date of Excel files
kpi_db_path = os.path.join(workspace_dir, "RET_KPI_Sales_Database.xlsx")
prod_db_path = os.path.join(workspace_dir, "RET_Product_Sales_Database.xlsx")

mtimes = []
if os.path.exists(kpi_db_path):
    mtimes.append(os.path.getmtime(kpi_db_path))
if os.path.exists(prod_db_path):
    mtimes.append(os.path.getmtime(prod_db_path))

if mtimes:
    latest_mtime = max(mtimes)
    last_update_dt = datetime.datetime.fromtimestamp(latest_mtime)
    formatted_date = last_update_dt.strftime("%A, %B %d, %Y")
else:
    formatted_date = datetime.datetime.now().strftime("%A, %B %d, %Y")

# Read data vars
data_vars_path = os.path.join(script_dir, "scratch", "data_vars.js")
template_path = os.path.join(script_dir, "template.html")

with open(data_vars_path, "r", encoding="utf-8") as f:
    data_vars_content = f.read()

# Read template HTML
with open(template_path, "r", encoding="utf-8") as f:
    template_content = f.read()

# Merge
final_content = template_content.replace("/* RETAIL_DATA_PLACEHOLDER */", data_vars_content)
final_content = final_content.replace("/* LAST_UPDATE_PLACEHOLDER */", formatted_date)

# Write to workspace
output_path = os.path.join(workspace_dir, "index.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(final_content)

print(f"Successfully compiled single-file dashboard at: {output_path}")
print(f"File size: {os.path.getsize(output_path) / 1024:.2f} KB")
