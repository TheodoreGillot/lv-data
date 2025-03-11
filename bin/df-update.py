import pandas as pd
import configparser
import os

config = configparser.ConfigParser()
config.read('../cfg/config.ini')

data_dir = config['DEFAULT'].get('data_dir')

os.chdir("/media/data/lvmh")

products_df = pd.read_csv('product_inf_2000.csv')
client_df = pd.read_csv('client_inf_2000.csv',sep=';')
transactions_df = pd.read_csv('transac_inf_2000.csv', sep=',')

products = pd.read_csv('product.csv')
client = pd.read_csv('client.csv', sep=';')
transactions = pd.read_csv('transac.csv', sep=';')

combined_products = pd.concat([products, products_df], ignore_index=True)

for col in products_df.columns:
    combined_products[col] = combined_products[col].astype(products_df[col].dtype)

combined_products.to_csv('updated_product.csv', index=False, sep=',', na_rep='')

combined_client = pd.concat([client, client_df], ignore_index=True)

for col in client_df.columns:
    combined_client[col] = combined_client[col].astype(client_df[col].dtype)

combined_client.to_csv('updated_client.csv', index=False, sep=',', na_rep='')

transactions_df = transactions_df.rename(columns={'website_version': 'country'})
combined_transactions = pd.concat([transactions, transactions_df], ignore_index=True)

for col in transactions_df.columns:
    combined_transactions[col] = combined_transactions[col].astype(transactions_df[col].dtype)
    
combined_transactions.to_csv('updated_transac.csv', index=False, sep=',', na_rep='')
