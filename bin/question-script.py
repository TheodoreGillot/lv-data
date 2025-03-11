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


print(transac.info())
print(client.info())
print(product.info())

def extract_year_week(df):
    df['year'] = df['week'].str[1:5].astype(int)
    df['week_number'] = df['week'].str[5:].astype(int)

for name, df in zip(['client', 'transac'], [client, transac]):
    extract_year_week(df)
    df.to_csv(f'/media/data/lvmh/{name}_splitted_week.csv', index=False)
    print(f"succesfully saved {name}_splitted_week.csv")
