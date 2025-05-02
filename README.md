# E-Commerce Data Analysis Project

This project showcases an end-to-end analysis of an e-commerce dataset using **Python** for data cleaning and exploration, and **Power BI** for interactive dashboarding and insights.

## Table of Contents
- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Steps Performed](#steps-performed)
- [Power BI Dashboard](#power-bi-dashboard)
- [Key Insights](#key-insights)
- [How to Run](#how-to-run)
- [Screenshots](#screenshots)

## Overview
The goal of this project is to analyze customer transactions to identify purchase patterns, top products, and high-value countries. The analysis involves:
- Cleaning missing data
- Aggregating metrics
- Visualizing top purchase dates, top products, and customer country distribution
- Building an interactive Power BI dashboard

## Technologies Used
- Python (Pandas, Matplotlib)
- Power BI Desktop
- Jupyter Notebook / PyCharm
- DAX (for calculated fields)

## Project Structure
ecommerce-analysis/ │ ├── data.csv                         # Raw data file ├── cleaned_ecom_data.csv            # Cleaned output data ├── ecom_analysis.py                 # Main Python script ├── Top purchase dates.png           # Output plot ├── Top products.png                 # Output plot ├── Top Countries purchase count.png # Output plot ├── Ecom_Dashboard.pbix              # Power BI dashboard file ├── README.md                        # Project documentation └── .gitignore                       # Git ignore settings

## Steps Performed

### In Python:
1. **Data Cleaning**
   - Replaced missing `CustomerID` with unique placeholders based on `InvoiceNo`
   - Filled missing `Description` with `"Not Mentioned"`

2. **Exploratory Analysis**
   - Top purchase dates by quantity
   - Top 10 products purchased
   - Top 10 countries by purchase count

3. **Visualization**
   - Line plot for top purchase dates
   - Bar chart for top products
   - Bar charts for top countries purchase counts

### In Power BI:
- Built interactive dashboard with:
  - **KPI Cards**: Total Revenue, Unique Customers, Avg Order Value
  - **Trend Sparklines**
  - **Tooltips**
  - **Slicers** for Year and Country

## Key Insights
- Top purchase spikes occurred on specific days
- Majority of purchases came from the United Kingdom
- A few products drive the majority of the sales volume

## How to Run
1. Clone this repository
2. Run `ecom_analysis.py` to generate cleaned data and visualizations
3. Open `Ecom_data_analysis.pbix` in Power BI Desktop to explore the dashboard

## Screenshots
> Include screenshots of your Power BI dashboard and matplotlib charts here.

---