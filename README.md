# Retail Performance Scorecard & Visual Report

An interactive, high-fidelity business intelligence dashboard that aggregates and visualizes multi-year retail store performance metrics. Fully offline-capable, highly responsive, and built using modern styling principles.

## Project Structure

The project has been organized to keep the root directory clean and professional:

```text
Retail/
├── Retail_Visual_Report.html       # The compiled interactive dashboard
├── RET_KPI_Sales_Database.xlsx     # KPI Database (Store performance metrics)
├── RET_Product_Sales_Database.xlsx # Product Database (Product group-level transactions)
├── README.md                       # Project documentation
└── Reference_Material/             # Core scripts, dataset vars, design assets, and logs
    ├── compile.py                  # Builds Retail_Visual_Report.html from template
    ├── prepare_data.py             # Pulls Excel records and regenerates compact vars
    ├── validate.py                 # Structural validator for compiled HTML
    ├── template.html               # The clean dashboard layout template
    ├── avatar.png                  # Headshot avatar image for Developer Modal
    └── scratch/
        └── data_vars.js            # Aggregated database records in JavaScript format
```

## Core Features

- **YoY Performance Comparison Matrix**: Displays Target Year vs Comparison Year (Target Year - 1) comparison for 10 key retail performance scorecard dimensions.
- **Dynamic Year-Slicing Engine**: When a year is selected, all matrix headers, YoY growth percentages, and chart datasets adapt automatically to target vs previous year.
- **Dynamic Filters**: Slices data dynamically by **Store Name**, **Target Year**, **Product Category**, and **Month/Season** (using a custom multi-select checkbox dropdown with shortcuts like Q1-Q4, SS, AW).
- **Interactive Visual Analytics**:
  - **Sales Monthly Performance**: Monthly Net Sales/Quantity trend line comparison.
  - **Product Categories Comparison**: Bar chart comparing categories with dynamic growth percentage labels.
  - **Share of Business**: Three side-by-side interactive doughnut charts showing share of contribution across Categories, Divisions, and Gender.
  - **Metric Toggles**: Switch between Net Sales ($) and Net Quantity (Units) instantly on all three charts.
- **Best Selling Product Groups Table**: Lists product group performance ranked descending, with interactive column headers to sort by Net Sales or Net Quantity.
- **Credits Modal**: A custom "About this Dashboard" overlay in the navigation bar displaying the developer profile, bio, headshot avatar, and LinkedIn link.

## Tech Stack

- **Frontend**: HTML5, Vanilla JavaScript, Chart.js (v4), Chart.js Datalabels Plugin (v2), Tailwind CSS (v4 - Modern CSS-first approach).
- **Backend Data Pipelines**: Python (v3), Pandas, Openpyxl.

## How to Run the Dashboard

Simply double-click the `Retail_Visual_Report.html` file to open it in any modern web browser. It is fully self-contained, requiring no hosting servers or external network connections to function (aside from loading external Chart.js libraries from a CDN, which is cached by the browser).

## How to Refresh/Update the Data

If the underlying Excel sheets (`RET_KPI_Sales_Database.xlsx` or `RET_Product_Sales_Database.xlsx`) are modified, you can rebuild the visual scorecard report by running these steps:

1. **Prerequisites**: Ensure you have Python and the required libraries installed:
   ```bash
   pip install pandas openpyxl
   ```
2. **Aggregated Database Refresh**: From the project directory, run:
   ```bash
   python Reference_Material/prepare_data.py
   ```
   *This loads the Excel databases, aggregates the product-level records by Product Group, and saves the data arrays in `Reference_Material/scratch/data_vars.js`.*
3. **Rebuild Visual Report**: Run the compiler script:
   ```bash
   python Reference_Material/compile.py
   ```
   *This merges `Reference_Material/template.html` and `data_vars.js` to output the new compiled `Retail_Visual_Report.html` at the root.*
4. **Validate**: Run the validation script to verify structure:
   ```bash
   python Reference_Material/validate.py
   ```

---
*Designed and Developed by Federico Bucayan | © 2026*
