


import requests
import base64

# Your Shopify store credentials
API_KEY = "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"
STORE_NAME = "ai-merch-project"
PRODUCT_ID = "9001025241303"  # Replace this with your actual product ID

# Path to your image file
image_path = "mockup_converted.jpg"

# Read and encode image in base64
with open(image_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

# Set API endpoint
url = f"https://{STORE_NAME}.myshopify.com/admin/api/2024-01/products/{PRODUCT_ID}/images.json"

# Prepare payload
payload = {
    "image": {
        "attachment": encoded_string
    }
}

# Headers
headers = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": API_KEY
}

# Make request
response = requests.post(url, json=payload, headers=headers)

# Output
if response.status_code == 201:
    print("✅ Image uploaded successfully!")
    print("🖼️ Image URL:", response.json()["image"]["src"])
else:
    print("❌ Failed to upload image:")
    print(response.text)

