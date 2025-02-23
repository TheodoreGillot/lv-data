import pandas as pd
import configparser
import os

config = configparser.ConfigParser()
config.read('../cfg/config.ini')

data_dir = config['DEFAULT'].get('data_dir')

product_df_path = os.path.join(data_dir, config['DEFAULT'].get('combined_product', fallback=None))
client_splitted_week_path = os.path.join(data_dir, config['DEFAULT'].get('client_splitted_week'))
transac_splitted_week_path = os.path.join(data_dir, config['DEFAULT'].get('transac_splitted_week'))

product = pd.read_csv(product_df_path, sep=',')
client_splitted_week = pd.read_csv(client_splitted_week_path, sep=',')
transac_splitted_week = pd.read_csv(transac_splitted_week_path, sep=',')

print(product.head())
print(client_splitted_week.columns)
print(transac_splitted_week.columns)

print(product['price_fr_eur'].min())
print(len(transac_splitted_week['product_id'].unique()))

merged_df = transac_splitted_week.merge(product[['product_id', 'macro_family', 'price_fr_eur']], on='product_id', how='left')

print(merged_df.columns)
print(merged_df['price_fr_eur'].max())
print(merged_df.head(10)
)

total_sales_2023 = merged_df[
    (merged_df['year'] == 2023) & 
    (merged_df['macro_family'] == 'CITY BAGS')
]['price_fr_eur'].sum()

print(int(total_sales_2023))