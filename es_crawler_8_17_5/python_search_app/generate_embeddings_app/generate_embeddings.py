from flask import Flask, request, render_template
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
from io import BytesIO
import torch
import requests

app = Flask(__name__)

# CLIP setup
device = "cuda" if torch.cuda.is_available() else "cpu"
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def generate_embedding(image):
    inputs = processor(images=image, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.get_image_features(**inputs)
    embedding = outputs / outputs.norm(p=2, dim=-1, keepdim=True)
    return embedding.cpu().numpy().flatten().tolist()

@app.route('/', methods=['GET', 'POST'])
def index():
    embeddings = None
    error = None

    if request.method == 'POST':
        image_file = request.files.get('image')
        image_url = request.form.get('image_url')

        try:
            if image_file:
                image = Image.open(image_file.stream).convert("RGB")
            elif image_url:
                response = requests.get(image_url)
                response.raise_for_status()
                image = Image.open(BytesIO(response.content)).convert("RGB")
            else:
                raise ValueError("No image provided!")

            embeddings = generate_embedding(image)

        except Exception as e:
            error = str(e)

    return render_template('index.html', embeddings=embeddings, error=error)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
