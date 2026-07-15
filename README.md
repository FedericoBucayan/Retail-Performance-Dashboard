# Retail Performance Scorecard & Visual Report

This is an interactive dashboard created to translate raw retail sales spreadsheets into a clean, modern visual report. It is designed to help analyze store performance, monitor product category contributions, and track Year-over-Year (YoY) commercial growth trends easily.

## What is in this Folder

To keep things neat and easy to manage, the project folder has been organized like this:

* **`Retail_Visual_Report.html`**: The interactive scorecard report. Just double-click this file to open it in any web browser. It runs locally on your PC without needing an internet connection.
* **`RET_KPI_Sales_Database.xlsx`**: The Excel spreadsheet containing store-level KPIs (Traffic, Transactions, Sales, Margins, and Basket metrics).
* **`RET_Product_Sales_Database.xlsx`**: The Excel spreadsheet detailing product-level sales.
* **`README.md`**: This help document.
* **`Reference_Material/`**: A folder containing background templates, data processing files, and design assets. You don't need to open this folder unless you are refreshing the database.

## Key Features

* **YoY Performance Matrix**: A table comparing Target vs Previous Year performance across 10 core retail metrics (including Sales, Quantities, ASP, Traffic, Conversion Rate, ATV, UPT, and Full Price mix).
* **Interactive Trend Charts**: Visual charts showing monthly sales curves and category comparisons. You can toggle between viewing **Sales ($)** or **Quantity (Units)** instantly.
* **Share of Business**: Three visual doughnut charts showing the percentage contribution of Product Categories, Merchandise Divisions, and Gender demographics for the selected year.
* **Best Sellers Ranking**: A list of your top product groups, which you can sort by Net Sales or Quantity.
* **Dynamic Filters**: Refine your scorecard view instantly by **Store**, **Target Year**, **Product Category**, or specific **Months/Seasons**.

## How to Update the Dashboard with New Data

If you update the Excel files with new sales records, you can refresh the dashboard by running these two commands in your command prompt:

1. **Aggregate the spreadsheet data**:
   ```bash
   python Reference_Material/prepare_data.py
   ```
2. **Rebuild the visual report**:
   ```bash
   python Reference_Material/compile.py
   ```
3. Open `Retail_Visual_Report.html` in your browser to see your updated dashboard!

---
*Designed and Developed by Federico Bucayan | © 2026*
