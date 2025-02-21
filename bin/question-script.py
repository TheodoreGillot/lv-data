import pandas as pd
import configparser

config = configparser.ConfigParser()
config.read('../cfg/config.ini')

product_df_path = config['DEFAULT'].get('product_df', fallback=None)
client_df_path = config['DEFAULT'].get('client_df', fallback=None)
transac_df_path = config['DEFAULT'].get('transac_df', fallback=None)

product = pd.read_csv(product_df_path, sep=',')
client = pd.read_csv(client_df_path, sep=';')
transac = pd.read_csv(transac_df_path, sep=',')


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

client_splitted_week_path = config['DEFAULT'].get('client_splitted_week', fallback=None)
transac_splitted_week_path = config['DEFAULT'].get('transac_splitted_week', fallback=None)

client_splitted_week = pd.read_csv(client_splitted_week_path, sep=',')
transac_splitted_week = pd.read_csv(transac_splitted_week_path, sep=',')

print(client_splitted_week.head())
print(transac_splitted_week.head())