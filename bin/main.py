import configparser
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder, RobustScaler, OneHotEncoder
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.compose import ColumnTransformer
import warnings
import re

warnings.filterwarnings('ignore')

# Load dataa
config = configparser.ConfigParser()
config.read('../cfg/config.ini')

product_df_path = config['DEFAULT'].get('product_df', fallback=None)
client_df_path = config['DEFAULT'].get('client_df', fallback=None)
transac_df_path = config['DEFAULT'].get('transac_df', fallback=None)

product_df = pd.read_csv(product_df_path, sep=',')
client_df = pd.read_csv(client_df_path, sep=';')
transac_df = pd.read_csv(transac_df_path, sep=';')

# Aggregations
transaction_aggs = transac_df.groupby('store_type_label').agg({
    'product_quantity': ['sum', 'mean', 'std'],
    'count_distinct_transaction': ['sum', 'mean']
}).reset_index()

# Flatten columns
transaction_aggs.columns = [
    f"{col[0]}_{col[1]}" if col[1] else col[0] 
    for col in transaction_aggs.columns
]

# Merge
merged_df = client_df.merge(transaction_aggs, on='store_type_label', how='left')

# Convert age ranges to numeric (extract lower bound)
merged_df['age'] = merged_df['age'].apply(lambda x: float(re.search(r'\d+', x).group()) if pd.notnull(x) else np.nan)

# Remplacer les valeurs manquantes par la médiane
merged_df['age'].fillna(merged_df['age'].median(), inplace=True)
# Feature engineering
merged_df['transactions_per_client'] = merged_df['count_distinct_transaction_sum'] / merged_df['clients']
merged_df['avg_quantity_per_transaction'] = merged_df['product_quantity_sum'] / merged_df['count_distinct_transaction_sum']
merged_df['transaction_variability'] = np.log1p(merged_df['product_quantity_std'] / merged_df['product_quantity_mean'])
merged_df['client_efficiency'] = merged_df['items_bought'] / merged_df['clients']

# Define features
categorical_features = ['nationality', 'gender', 'universe', 'macro_family', 'is_reachable', 'store_type_label', 'store_zone']
numerical_features = ['age', 'transactions_per_client', 'avg_quantity_per_transaction', 'transaction_variability', 'client_efficiency']

# Convert age to numeric
merged_df['age'] = pd.to_numeric(merged_df['age'], errors='coerce').fillna(merged_df['age'].median())

# One-hot encoding
encoder = ColumnTransformer([("cat", OneHotEncoder(handle_unknown='ignore'), categorical_features)], remainder='passthrough')

# Remove outliers
def remove_outliers(df, columns, n_std=3):
    df_clean = df.copy()
    for col in columns:
        mean = df_clean[col].mean()
        std = df_clean[col].std()
        df_clean = df_clean[~((df_clean[col] - mean).abs() > n_std * std)]
    return df_clean

merged_df = remove_outliers(merged_df, numerical_features)

# Prepare features
feature_cols = categorical_features + numerical_features
X = merged_df[feature_cols]
y = merged_df['items_bought']

# Scale numerical features
scaler = RobustScaler()
X[numerical_features] = scaler.fit_transform(X[numerical_features])
X = encoder.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train Random Forest model
rf_model = RandomForestRegressor(
    n_estimators=100,
    max_depth=8,  # Reduced from 10 to prevent overfitting
    min_samples_split=10,  # Increased for generalization
    min_samples_leaf=4,  # Increased to smooth decision boundaries
    random_state=42
)

rf_model.fit(X_train, y_train)

y_pred = rf_model.predict(X_test)

# Metrics
print("\nModel Performance Metrics:")
print(f"R2 Score: {r2_score(y_test, y_pred):.3f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.3f}")
print(f"RMSE as % of mean: {(np.sqrt(mean_squared_error(y_test, y_pred))/y.mean()*100):.2f}%")

# Cross-validation
cv_scores = cross_val_score(rf_model, X, y, cv=5, scoring='r2')
print(f"\nCross-validation R2: {cv_scores.mean():.3f} (+/- {cv_scores.std() * 2:.3f})")
