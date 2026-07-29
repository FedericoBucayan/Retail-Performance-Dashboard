# Retail Performance Dashboard

🌐 [Live Interactive Dashboard Demo](https://federicobucayan.github.io/Retail-Performance-Dashboard/)

An end-to-end retail analytics solution built as a **live interactive web dashboard (`index.html`)** — a fully self-contained visual report that aggregates multi-year sales spreadsheets, calculates commercial KPIs dynamically, and displays store, category, and product-level insights in a clean corporate interface.

This repository was designed specifically as a portfolio showcase for recruiters, hiring managers, and retail & supply chain leaders.

---

## 🎯 Executive Value Proposition (For Recruiters & Hiring Managers)

### 1. 📈 Retail & Supply Chain Planning Expertise & Decision-Maker Mindset
First and foremost, this project demonstrates deep functional expertise in retail commercial analytics and supply chain planning performance measurement:
* **Core KPI Analysis**: Calculates and visualizes key retail planning metrics dynamically — including **Net Sales (NS)**, **Net Quantity (NQ)**, **Year-over-Year (YoY) Growth**, **Average Selling Price (ASP)**, **Standard Margin % (SM%)**, **Conversion Rate (CR%)**, **Units Per Transaction (UPT)**, **Average Transaction Value (ATV)**, and **Full Price Mix %**.
* **Multi-Dimensional Breakdown**: Analyses commercial performance across stores, product categories, merchandise divisions, gender demographics, and product groups — with full YoY comparison at every level.
* **Decision-Support Architecture**: Built from the perspective of an experienced retail and supply chain planning practitioner and decision-maker. The dashboard is engineered to translate raw sales databases into actionable commercial insights, facilitating strategic decisions around product assortment, channel performance, markdown strategy, and inventory planning.

### 2. 🤖 AI-Powered Engineering & Digital Mindset (Co-Created with Google Antigravity)
Second, this repository showcases a forward-thinking digital mindset and passion for modern technology:
* **Transparency Statement**: I built this entire project combining my expertise in retail planning and commercial analytics in partnership with **Google Antigravity** (an advanced agentic AI coding assistant).
* **Bridging Data Analytics & Software Engineering**: While I am highly proficient in commercial KPI design, spreadsheet database management, and business intelligence, I leveraged agentic AI to bridge the gap into full-stack software development — orchestrating Python ETL automation, web application design (HTML5/JS), and an automated build and validation pipeline.
* **AI Enthusiast & Early Adopter**: Demonstrates my eagerness to learn, master, and integrate cutting-edge AI tools into daily workflows — bringing a curious, innovative, and digital-first mindset to any progressive organization.

---

## 🛠️ Key Dashboard Capabilities & Features

### 1. YoY Performance Comparison Matrix
A full-page comparison matrix showing current year vs. prior year performance per store and in total, across all core KPIs (NS, NQ, ASP, SM%, Traffic, Transactions, CR%, ATV, UPT, FP Mix%). All YoY movements are color-coded with directional badges (▲/▼).

### 2. Sales Monthly Performance Trend
An interactive line chart overlaying current year vs. prior year monthly sales or quantity — with a Sales ($) / Qty (Units) toggle and a custom multi-month checkbox filter including seasonal (SS, FW) and quarterly (Q1–Q4) quick-select shortcuts.

### 3. Categories / Divisions / Gender Comparison Chart
An interactive bar chart with a **dimension toggle** (Category, Division, Gender) that dynamically regroups and redraws the chart — with per-bar YoY growth labels and a detailed tooltip showing both **NS YoY Growth %** and **NQ YoY Growth %** on hover.

### 4. Share of Business Doughnut Charts
Three side-by-side doughnut charts showing the percentage contribution to total sales or quantity by **Categories**, **Divisions**, and **Gender** — with a Sales / Qty metric toggle.

### 5. Product Group Benchmarks Table
A sortable breakdown table by Category, Division, or Gender segment with NS, YoY Sales growth, NQ, YoY Qty growth, and Margin % — dynamically switching between breakdown dimensions.

### 6. Best Selling Product Groups Ranking
A dynamic ranking table of all product groups sortable by Net Sales or Net Quantity, displaying NS, **Sales YoY Growth**, NQ, **Qty YoY Growth**, and Margin % with color-coded growth badges.

---

## 💻 Tech Stack & Pipeline

* **Backend / ETL**: Python 3 (Pandas, Openpyxl) — aggregates raw Excel databases and outputs compact data arrays.
* **Web Application**: HTML5, Vanilla JavaScript, Chart.js (v4), Chart.js Datalabels Plugin (v2), Tailwind CSS (v4).
* **Build Pipeline**: Automated `.bat` script that runs data preparation, HTML compilation, validation checks, and launches the report in one click.

---

## 📂 Repository File Guide

* **`index.html`**: The main compiled interactive visual dashboard. Open this to view the report.
* **`Refresh_Retail_Visual_Report.bat`**: One-click batch script to aggregate spreadsheet data, compile the dashboard layout, run validation, and launch the report.
* **`RET_KPI_Sales_Database.xlsx`**: Store-level KPI spreadsheet database.
* **`RET_Product_Sales_Database.xlsx`**: Product transaction-level spreadsheet database.
* **`Reference_Material/`**: Source template, Python pipeline scripts, and build assets.
* **`README.md`**: Project documentation (this file).

---
*Designed and Developed by Federico Bucayan | © 2026*
