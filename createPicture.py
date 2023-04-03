import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create image with input
def create(prompt):
    openai.api_key = os.getenv('OPENAI_API_KEY')

    response = openai.Image.create(
        prompt = prompt,
        n=1,
        size = "512x512"
    )
    image_url = response["data"][0]["url"]

    return (image_url)

