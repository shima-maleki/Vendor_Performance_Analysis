# 📊 Vendor Performance Analysis
This project is an end-to-end data analysis and visualization pipeline focused on assessing and improving vendor performance. It showcases data cleaning, exploratory data analysis, and dashboarding using real-world data patterns. Built to highlight proficiency in Python, SQL, data wrangling, and BI tools.

# 🏗️ Architecture

This project follows a modular and scalable architecture designed to support an end-to-end data analysis workflow.

![Architecture](visuals/powerbid.jpg)


# 🧠 Objective
The primary goal of this project is to:

- Evaluate the performance of different vendors using historical data.

- Identify patterns, trends, and potential outliers.

- Provide actionable insights through visual dashboards to support business decisions.

# 📁 Project Structure
```
VENDOR_PERFORMANCE_ANALYSIS/
│
├── dashboard/                   # Power BI dashboard file
│   └── powerbi_dashboard.pbix
│
├── data/                        # Raw or intermediate data
│
├── logs/                        # Execution logs
│   └── get_vendor_summary.log
│
├── notebooks/                  # Jupyter Notebooks for stepwise analysis
│   ├── 01_data_cleaning.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   └── 03_Vendor_Performance_Analysis.ipynb
│
├── reports/                    # Final markdown report
│   └── Report.md
│
├── src/                        # Python modules
│   ├── infrastructure/         # Database connection utilities
│   │   ├── mysql_connection.py
│   │   └── postgres_connection.py
│   ├── pipelines/              # Data processing pipelines
│   │   ├── data_ingestion.py
│   │   ├── ingest_data.py
│   │   └── vendor_summary.py
│   └── config.py               # Configuration variables
│
├── visuals/                    # Image outputs for insights
│   └── churn_dashboard.png
│
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── LICENSE                     # License info
└── .gitignore
```

# 🔍 Key Features
**Data Cleaning:** Handling missing values, outliers, and formatting.

**EDA:** Vendor churn rate, volume trends, quality indicators.

**SQL Integration:** Modular MySQL and PostgreSQL connection utilities.

**Pipelines:** Python-based data ingestion and summary generation.

**Visualization:** Power BI dashboard to highlight key insights.

**Automation Logs:** Logging to track data pipeline execution.

# 🚀 How to Run
1. Clone the repository
```
git clone https://github.com/yourusername/VENDOR_PERFORMANCE_ANALYSIS.git
cd VENDOR_PERFORMANCE_ANALYSIS
```

2. Create and activate a virtual environment

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Run notebooks or pipelines

- Use JupyterLab or VSCode to run notebooks/.

- Or execute scripts inside src/pipelines/ for modular pipeline runs.

# 📊 POWER BI Dashboard

![POWERBIREPORT](visuals/powerBIREPORT.png)

# 📊 Analysis Visuals

| [![Top 10 Vendors](visuals/top10venders.png)](visuals/top10venders.png) | [![Vendor Contribution](visuals/vendorcontribution.png)](visuals/vendorcontribution.png) |
|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| **Top 10 Vendors by Performance**                                        | **Vendor Contribution to Overall Sales**                                                 |
| [![Confidence Interval](visuals/confidence_interval.png)](visuals/confidence_interval.png) | [![Promotion Brands](visuals/promotionbrands.png)](visuals/promotionbrands.png) |
| **Confidence Interval for Vendor Metrics**                               | **Brand Promotions Distribution**                                                        |


# 🧰 Tools & Technologies
**Languages:** Python (Pandas, NumPy, Scipy), SQL

**BI Tools:** Power BI

**Database:** MySQL, PostgreSQL

**Visualization:** Matplotlib, Seaborn

**Environment:** Jupyter, VSCode, Virtualenv

# 🧑‍💻 About Me
I’m a data enthusiast with hands-on experience in building data pipelines, performing EDA, and delivering business insights through dashboards. This project is part of my effort to demonstrate real-world problem solving using data.

📧 [shimamaleki95@yahoo.com]

🔗 [LinkedIn](https://www.linkedin.com/in/malekishima/)

# 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.
