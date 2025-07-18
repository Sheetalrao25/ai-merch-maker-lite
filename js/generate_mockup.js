const fs = require('fs');
const path = require('path');
const { createCanvas, loadImage } = require('canvas');


const TEMPLATE_PATH = path.join(__dirname, '../assets/template.jpeg');
const PRODUCT_PATH = path.join(__dirname, '../sample_outputs/product.png');
const OUTPUT_PATH = path.join(__dirname, '../sample_outputs/mockup.png');
const JSON_OUTPUT = path.join(__dirname, '../sample_outputs/mockup.json');



async function createMockup() {
  const canvas = createCanvas(800, 800);
  const ctx = canvas.getContext('2d');
  const template = await loadImage(TEMPLATE_PATH);
  const product = await loadImage(PRODUCT_PATH);



  // Draw base template
  ctx.drawImage(template, 0, 0, 800, 800);

  // Overlay product image (adjust position/size as needed)
  ctx.drawImage(product, 200, 200, 400, 400);

  
  // Save final image
  const buffer = canvas.toBuffer('image/png');
  fs.writeFileSync(OUTPUT_PATH, buffer);

  // Save response JSON
  const result = {
    mockup_url: OUTPUT_PATH,
    product_id: "mock123",
    variant: "t-shirt",
    image_position: "center"
  };

  fs.writeFileSync(JSON_OUTPUT, JSON.stringify(result, null, 2));
  console.log("✅ Mockup image and mockup.json saved.");
}



createMockup();
const fs = require('fs');
const path = require('path');




const mockup = {
  mockup_url: path.resolve(__dirname, '../sample_outputs/mockup.png'),
  product_id: 'mock123',
  variant: 't-shirt',
  image_position: 'center',
  caption: 'A white t-shirt with a pixel cartoon character',
  tags: ['white', 'shirt', 'cartoon', 'character', 'pixel', 'pikachu']
};

fs.writeFileSync(
  path.resolve(__dirname, '../sample_outputs/mockup.json'),
  JSON.stringify(mockup, null, 2)
);

