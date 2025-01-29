import pandas as pd
import configparser

class DataCleaner:
    def __init__(self, config_path):
        config = configparser.ConfigParser()
        config.read(config_path)
        self.product_df_path = config['DEFAULT'].get('product_df', fallback=None)
        self.client_df_path = config['DEFAULT'].get('client_df', fallback=None)
        self.transac_df_path = config['DEFAULT'].get('transac_df', fallback=None)
        self.load_data()

    def load_data(self):
        self.product_df = pd.read_csv(self.product_df_path, sep=',')
        self.client_df = pd.read_csv(self.client_df_path, sep=';')
        self.transac_df = pd.read_csv(self.transac_df_path, sep=';')

    def clean_client_data(self):
        self.client_df.drop_duplicates(inplace=True)
        self.client_df.fillna({
            'sku_description': 'Unknown',
            'marketing_color': 'Unknown',
            'main_material': 'Unknown',
            'collection': 'Unknown',
            'aesthetic_line': 'Unknown'
        }, inplace=True)

    def clean_product_data(self):
        if 'week;nationality;gender;universe;macro_family;is_reachable;age;is_big_client;store_type_label;store_zone;clients;items_bought' in self.product_df.columns:
            self.product_df[['week', 'nationality', 'gender', 'universe', 'macro_family', 'is_reachable', 'age', 'is_big_client', 'store_type_label', 'store_zone', 'clients', 'items_bought']] = self.product_df['week;nationality;gender;universe;macro_family;is_reachable;age;is_big_client;store_type_label;store_zone;clients;items_bought'].str.split(';', expand=True)
            self.product_df.drop(columns=['week;nationality;gender;universe;macro_family;is_reachable;age;is_big_client;store_type_label;store_zone;clients;items_bought'], inplace=True)
        self.product_df.drop_duplicates(inplace=True)

    def clean_transac_data(self):
        if 'week;product_id;store_type_label;country;count_distinct_transaction;product_quantity' in self.transac_df.columns:
            self.transac_df[['week', 'product_id', 'store_type_label', 'country', 'count_distinct_transaction', 'product_quantity']] = self.transac_df['week;product_id;store_type_label;country;count_distinct_transaction;product_quantity'].str.split(';', expand=True)
            self.transac_df.drop(columns=['week;product_id;store_type_label;country;count_distinct_transaction;product_quantity'], inplace=True)
        self.transac_df.drop_duplicates(inplace=True)

    def save_cleaned_data(self):
        self.client_df.to_csv('/media/data/lvmh/cleaned_client.csv', index=False)
        self.product_df.to_csv('/media/data/lvmh/cleaned_product.csv', index=False)
        self.transac_df.to_csv('/media/data/lvmh/cleaned_transac.csv', index=False)

    def clean_all_data(self):
        self.clean_client_data()
        self.clean_product_data()
        self.clean_transac_data()
        self.save_cleaned_data()

cleaner = DataCleaner('../cfg/config.ini')
cleaner.clean_all_data()
