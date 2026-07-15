# Retail Performance Scorecard & Visual Report

An interactive YoY retail dashboard that aggregates multi-year sales spreadsheets, calculates commercial metrics dynamically, and displays store and category insights in a clean corporate visual interface.

## 🤖 Co-Created with AI (Vibe Coding Showcase)

### Transparency Statement
I built this entire project acting as the product manager and system coordinator in partnership with Google Antigravity (an agentic AI coding assistant).

Instead of writing the code line-by-line, I used natural language instructions ("vibe coding") to guide the AI to implement:
* **Dynamic Year-Slicing Engine**: Year-agnostic calculations that update YoY matrix comparisons, table headers, and datasets dynamically based on the selected year.
* **Interactive Metric Toggles**: Toggles for Trend, Category, and Share charts to switch from Sales ($) to Quantity (Units) on-the-fly.
* **Contribution Pie Charts**: Dynamic percentage contributions rendered directly on interactive doughnut charts (utilizing the Chart.js Datalabels plugin).
* **Interactive Best Sellers Ranking**: A ranking list of product groups sortable by sales or quantity.
* **Custom Months/Seasons Filter**: A checkbox dropdown filter featuring seasonal (SS, AW) and quarterly (Q1-Q4) quick-select shortcuts.
* **Corporate Tailwind Styling**: Modern light-mode styling utilizing a sleek slate and white color scheme with navy and emerald highlights.

This repository demonstrates the power of AI-assisted engineering and showcases how a retail and supply chain expert can orchestrate, test, and deploy a fully functional dashboard application from scratch.

---

## 🛠️ How It Works (The Pipeline)

1. **Spreadsheet Inputs**: The database consists of two core Excel files: `RET_KPI_Sales_Database.xlsx` (store metrics) and `RET_Product_Sales_Database.xlsx` (product-level transactions).
2. **Database Aggregator**: Python loads the Excel records, aggregates the product-level database by Product Group, and outputs compact data arrays to `Reference_Material/scratch/data_vars.js`.
3. **HTML Compiler**: A compiler script merges the aggregated data variables directly with `Reference_Material/template.html` to generate a single compiled file.
4. **Interactive Dashboard**: Launches a fully self-contained visual report (`Retail_Visual_Report.html`) that runs offline in any browser.

## How to Update the Dashboard with New Data

If you update the Excel files with new sales records, you can refresh the dashboard in one of two ways:

### Method A: One-Click Update (Recommended)
Simply double-click the **`Refresh_Retail_Visual_Report.bat`** file in the root folder. This will automatically:
1. Aggregate the raw database spreadsheets.
2. Recompile the dashboard template.
3. Verify file integrity using the validation checks.
4. Open the updated **`Retail_Visual_Report.html`** in your default web browser.

### Method B: Manual Command Line Update
If you prefer running it manually from your terminal:
1. **Aggregate the spreadsheet data**:
   ```bash
   python Reference_Material/prepare_data.py
   ```
2. **Rebuild the visual report**:
   ```bash
   python Reference_Material/compile.py
   ```

---

## 💻 Tech Stack

* **Backend/ETL**: Python 3.11, Pandas, Openpyxl.
* **Frontend**: HTML5, Vanilla JavaScript, Chart.js (v4), Chart.js Datalabels Plugin (v2), Tailwind CSS (v4 - Modern CSS-first approach).

---

## 📂 Repository File Guide

* **`Retail_Visual_Report.html`**: The main compiled interactive visual dashboard. Open this to view the report.
* **`Refresh_Retail_Visual_Report.bat`**: One-click batch script to aggregate spreadsheet data, compile the dashboard layout, run validation, and launch the report.
* **`RET_KPI_Sales_Database.xlsx`**: Store-level KPI spreadsheet database.
* **`RET_Product_Sales_Database.xlsx`**: Product transaction-level spreadsheet database.
* **`README.md`**: Project documentation (this file).
* **`Reference_Material/`**: Subfolder housing the local data prep scripts, layout templates, and dashboard assets.

---
*Designed and Developed by Federico Bucayan | © 2026*
