# 🛍️ AI Merch Maker Lite

AI-powered mini project that **generates, designs, and publishes a merch product** from scratch using Python, Node.js, PHP, and now **Shopify API integration**.

---

## 💡 Features

✅ Generate product idea and description using AI (Python)  
✅ Generate product image using AI (Python)  
✅ Create T-shirt mockup with design (Node.js + Canvas)  
✅ Auto-generate captions & tags (Python Bonus)  
✅ Display product preview and simulate publishing (PHP frontend)  
✅ Upload and publish product to **Shopify developer store via API**

---

## 🛠 Tech Stack

| Layer        | Technology         | Purpose                              |
|--------------|--------------------|--------------------------------------|
| 🧠 AI Logic   | Python              | Product idea, image, tags, captions  |
| 🎨 Mockups   | Node.js + Canvas   | Image composition and rendering      |
| 🌐 Frontend | PHP + HTML/CSS     | UI to simulate product launch        |
| 🛒 Integration | Shopify API         | Programmatic product upload          |

---

## 🔄 Full Workflow

1. 🧠 **Generate Product Idea**  
   - Use Python (`generate_product.py`) to generate title & description

2. 🖼️ **Generate AI Image**  
   - Use Python (`generate_image.py`) to create product image

3. 🎨 **Create T-Shirt Mockup**  
   - Use Node.js script to generate a T-shirt mockup from image

4. 🏷️ **Auto-Generate Tags**  
   - Extract relevant hashtags and keywords from description/image

5. 🌍 **Display via PHP UI**  
   - Preview product in a clean frontend (`php/index.php`)

6. 🛒 **Upload to Shopify Store (NEW)**  
   - Use Shopify Admin API to:
     - Create a product with AI details
     - Upload the mockup image
     - Attach the image to the created product
       
👤 Author
Sheetal Rao
