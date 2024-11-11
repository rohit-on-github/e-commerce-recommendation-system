# src/recommendation.py

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def content_based_recommender(customer_id, product_data, top_n=5):
    # TF-IDF vectorization for product descriptions
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(product_data['description'])
    
    # Similarity matrix
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    # Find similar products for given customer ID
    recommended_product_indices = cosine_sim[customer_id].argsort()[-top_n:]
    return product_data.iloc[recommended_product_indices]

def collaborative_filtering_recommender(data, customer_id, top_n=5):
    # Simple collaborative filtering based on purchase history
    customer_purchases = data[data['customer_id'] == customer_id]
    similar_customers = data[data['product_id'].isin(customer_purchases['product_id'])]
    top_products = similar_customers['product_id'].value_counts().head(top_n).index
    return top_products

# Example usage
# product_recommendations = content_based_recommender(customer_id, product_data)
# collaborative_recommendations = collaborative_filtering_recommender(processed_data, customer_id)
