import requests
import json
import os

SHOPIFY_STORE = "ai-merch-project.myshopify.com"
ACCESS_TOKEN = " "  # ← your private token

def upload_to_shopify(title, description, price, image_url, sku="AI-SHIRT-001"):
    url = f"https://{SHOPIFY_STORE}/admin/api/2023-07/products.json"

    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": ACCESS_TOKEN
    }

    product_data = {
        "product": {
            "title": title,
            "body_html": description,
            "vendor": "AI Merch Maker",
            "product_type": "T-Shirt",
            "variants": [
                {
                    "price": price,
                    "sku": sku
                }
            ],
            "images": [
                {
                    "src": image_url
                }
            ]
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(product_data))

    if response.status_code == 201:
        print("✅ Product uploaded successfully!")
        print("Product ID:", response.json()["product"]["id"])
        return response.json()["product"]["id"]
    else:
        print("❌ Failed to upload product")
        print(response.text)
        return None
