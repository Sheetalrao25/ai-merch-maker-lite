import random
import json
import shutil
import os

TITLES = [
    "Funny Cat Mug", "Space Explorer Hoodie", "Motivational Quote T-shirt",
    "Pixel Art Coffee Cup", "Cyberpunk Mouse Pad"
]

DESCRIPTIONS = [
    "This stylish mug features an adorable cat meme—perfect for coffee lovers!",
    "A hoodie that takes you on a journey through the stars.",
    "Stay inspired with this T-shirt featuring bold, motivational text.",
    "Level up your mornings with pixel-perfect design on this mug.",
    "Bring neon vibes to your desk with this cyberpunk-themed mouse pad."
]

TAGS = [
    ["cat", "funny", "mug", "gift", "coffee"],
    ["space", "galaxy", "hoodie", "stars", "explorer"],
    ["quote", "tshirt", "inspiration", "text", "motivational"],
    ["pixel", "gaming", "cup", "retro", "design"],
    ["cyberpunk", "neon", "mousepad", "tech", "glow"]
]

IMAGE_FILES = [
    "cat.jpeg", "space.jpeg", "quote.jpeg", "pixel.jpeg", "cyberpunk.jpeg"
]

def generate_fake_product():
    idx = random.randint(0, 4)
    
    product = {
        "title": TITLES[idx],
        "description": DESCRIPTIONS[idx],
        "tags": TAGS[idx],
        "image_path": "sample_outputs/product.png"
    }

    # Copy matching image to sample_outputs
    src_image = os.path.join("assets", IMAGE_FILES[idx])
    dst_image = os.path.join("sample_outputs", "product.png")
    shutil.copy(src_image, dst_image)

    with open("sample_outputs/product.json", "w") as f:
        json.dump(product, f, indent=2)

    print("✅ Product JSON and image saved to sample_outputs/")

if __name__ == "__main__":
    generate_fake_product()
