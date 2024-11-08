# src/segmentation.py

from sklearn.cluster import KMeans
import pandas as pd

def customer_segmentation(data, n_clusters=5):
    # Using KMeans for clustering customers
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    data['cluster'] = kmeans.fit_predict(data[['purchase_amount']])
    
    return data

# Example usage
# clustered_data = customer_segmentation(processed_data)
