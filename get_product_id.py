# get_product_id.py
import requests

store_url = "ai-merch-project.myshopify.com"
access_token = "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"

url = f"https://{store_url}/admin/api/2023-07/products.json"
headers = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": access_token
}

response = requests.get(url, headers=headers)
products = response.json()["products"]

for product in products:
    print(f"{product['title']} --> ID: {product['id']}")
