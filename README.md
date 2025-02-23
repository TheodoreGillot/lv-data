# lv-data BDD project

## Features

- **Data understanding and cleaning**
- **Deep ML analysis**.
- **Detailed Reporting**

## Installation

Clone the repository:

```bash
git clone https://github.com/TheodoreGillot/lv-data.git
cd lv-data
```

Ensure Python (3.7 or later) is installed. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Configure your data directory in the cfg/config.ini file with the 6 spreadsheets:

## Usage

### Cleaning

Run the first script to clean and combine datasets:

```bash
python df_update.py
```

### Analysis

We have two basic python scripts:

```bash
python question-script.py
python sale-script.py
```

And two completed notebook with a ML analysis script:

```bash
jupyter nbconvert --to html --execute albert_school_notebook_complete.ipynb --ExecutePreprocessor.timeout=-1
jupyter nbconvert --to html --execute description_analysis.ipynb --ExecutePreprocessor.timeout=-1
```

## Output

After running the script, you'll receive 2 html outputs detailing:

- Data Integration: Combines datasets on products, transactions, and client behaviors, harmonizing structures for consistent analysis.

- Exploratory Data Analysis (EDA): Examines sales distributions, temporal trends, and product popularity across different dimensions (e.g., country, category, sales channel).

- Client Segmentation: Performs KMeans clustering to identify distinct customer segments based on purchasing habits and client characteristics.

- Time-Series Forecasting: Implements ARIMA and XGBoost models to forecast future product sales, comparing predictive accuracy with metrics like MAPE.

- Feature Engineering: Generates new variables (e.g., normalized items purchased, weekly/monthly aggregations, sales amounts) to deepen analytical insights.

- Sales Analysis by Channel: Compares online vs. physical store sales, highlighting differences in product popularity and sales trends.

- Behavioral Prediction: Utilizes Decision Tree models to identify client groups most likely to purchase specific product categories (e.g., TRAVEL products).

- Price Sensitivity Analysis: Explores the relationship between pricing and product demand to understand price elasticity.

- Product Segmentation: Applies KMeans to classify products into clusters based on popularity and pricing, identifying segments like bestsellers and high-end products.

- Visualization and Insights: Provides clear visual representations (histograms, line plots, scatter plots) that facilitate intuitive understanding of complex sales and customer behavior patterns.