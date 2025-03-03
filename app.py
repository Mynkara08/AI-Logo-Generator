from flask import Flask, render_template, request, url_for
from dotenv import load_dotenv
import openai
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_logo_image(user_input):
    """Generates an image using OpenAI's DALL·E API and returns the image URL."""
    client = openai.OpenAI()  
    response = client.images.generate(
        model="dall-e-3",
        prompt=f"Create onle and only one professional, minimalistic, and visually appealing logo with the theme: {user_input}. The logo should be simple, clean, and suitable for branding.",  
        n=1,  # Generate one image
        size="1024x1024"  # Image resolution
    )
    return response.data[0].url  # Return the generated image URL

@app.route('/', methods=['GET', 'POST'])
def index():
    logo_url = None
    if request.method == 'POST':
        user_input = request.form.get('logo_text', '').strip()  
        if user_input:
            logo_url = get_logo_image(user_input)  # Get generated image URL
    return render_template('index.html', logo_url=logo_url)

if __name__ == '__main__':
    app.run(debug=True)  # Keep only for development
