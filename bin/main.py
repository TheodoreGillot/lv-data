import configparser
import pandas as pd
import numpy as np

config = configparser.ConfigParser()
config.read('../cfg/config.ini')

product_df_path = config['DEFAULT'].get('product_df', fallback=None)
client_df_path = config['DEFAULT'].get('client_df', fallback=None)
transac_df_path = config['DEFAULT'].get('transac_df', fallback=None)

product_df = pd.read_csv(product_df_path)
client_df = pd.read_csv(client_df_path)
transac_df = pd.read_csv(transac_df_path)

print(product_df.info())
print(client_df.info())
print(transac_df.info())
