# src/app.py

from flask import Flask, request, jsonify
from recommendation import content_based_recommender, collaborative_filtering_recommender
import pandas as pd

app = Flask(__name__)

# Load sample data (replace with actual paths)
product_data = pd.read_csv('products.csv')
processed_data = pd.read_csv('processed_data.csv')

@app.route('/recommend', methods=['GET'])
def recommend():
    customer_id = int(request.args.get('customer_id'))
    method = request.args.get('method', 'collaborative')  # Default to collaborative filtering
    
    if method == 'content':
        recommendations = content_based_recommender(customer_id, product_data)
    else:
        recommendations = collaborative_filtering_recommender(processed_data, customer_id)
    
    return jsonify(recommendations.tolist())

if __name__ == '__main__':
    app.run(debug=True)
