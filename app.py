# backend/app.py
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

# Load data from Excel file
df = pd.read_excel('/mnt/data/PricingReport_20240516_203315894_4588.xlsx', sheet_name='05-16-2024 Pricing')

# Prepare the data
products = df[['Product ID', 'Product Name', 'Unit Price']].to_dict(orient='records')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    results = [product for product in products if query.lower() in product['Product Name'].lower() or query in str(product['Product ID'])]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
