import pandas as pd
import configparser
import os

config = configparser.ConfigParser()
config.read('../cfg/config.ini')

data_dir = config['DEFAULT'].get('data_dir')

product_df_path = os.path.join(data_dir, config['DEFAULT'].get('combined_product', fallback=None))
client_df_path = os.path.join(data_dir, config['DEFAULT'].get('combined_client'))
transac_df_path = os.path.join(data_dir, config['DEFAULT'].get('combined_transac'))

product = pd.read_csv(product_df_path, sep=',')
client = pd.read_csv(client_df_path, sep=';')
transac = pd.read_csv(transac_df_path, sep=';')


print(product.info())
print("-"*50)
print(client.info())
print("-"*50)
print(transac.info())
print("-"*50)
print(client.head())
print("-"*50)
print(transac.head())
print("-"*50)
print(product.head())
