# lv-data BDD project

## Overview

**lv-data** is a Python-based utility designed to compare datasets stored in CSV format. It identifies and highlights differences between two datasets—typically referred to as "old" and "new"—ensuring data consistency and accuracy. This tool is particularly useful for scenarios involving large, frequently updated datasets where efficiently tracking changes is crucial.

## Features

- **Dataset Comparison:** Quickly identifies differences between two CSV files.
- **Sorting and Validation:** Automatically sorts data by serial number and validates counts across datasets.
- **Detailed Reporting:** Provides clear reports on mismatches or discrepancies.

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

## Usage

Run the main script to compare datasets:

```bash
python compare_csv.py path/to/old_dataset.csv path/to/new_dataset.csv
```

### Example

```bash
python compare_csv.py data/previous.csv data/latest.csv
```

## Output

After running the script, you'll receive output detailing:
- Rows present only in the new dataset.
- Rows removed since the previous dataset.
- Any mismatches in count totals.