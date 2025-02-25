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

We have basic python scripts like:

```bash
python question-script.py
python sale-script.py
```

And  completed notebook with a ML analysis script, you can execute them for example with:

```bash
jupyter nbconvert --to html --execute albert_school_notebook_complete.ipynb --ExecutePreprocessor.timeout=-1
jupyter nbconvert --to html --execute description_analysis.ipynb --ExecutePreprocessor.timeout=-1
```

## Output

After running the script, you'll receive 2 html outputs detailing:

- Data Integration

- Exploratory Data Analysis

- Client Segmentation

- Time-Series Forecasting

- Sales Analysis by Channel

- Behavioral Prediction

- Product Segmentation

- Visualization and Insights