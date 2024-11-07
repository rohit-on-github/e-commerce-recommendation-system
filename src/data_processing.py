# src/data_processing.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_clean_data(customer_data_path, product_data_path):
    # Load data
    customer_data = pd.read_csv(customer_data_path)
    product_data = pd.read_csv(product_data_path)
    
    # Drop duplicates and handle missing values
    customer_data = customer_data.drop_duplicates().dropna()
    product_data = product_data.drop_duplicates().dropna()
    
    return customer_data, product_data

def preprocess_data(customer_data, product_data):
    # Merge or process data as needed for model training
    data = customer_data.merge(product_data, on="product_id", how="inner")
    data = data[['customer_id', 'product_id', 'purchase_amount']]
    
    # Feature scaling for clustering
    scaler = StandardScaler()
    data[['purchase_amount']] = scaler.fit_transform(data[['purchase_amount']])
    
    return data

# Example usage
# customer_data, product_data = load_and_clean_data('customers.csv', 'products.csv')
# processed_data = preprocess_data(customer_data, product_data)
