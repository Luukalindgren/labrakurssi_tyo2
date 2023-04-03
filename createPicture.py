import openai
import os
from dotenv import load_dotenv
from discord.ext import commands

# Load environment variables
load_dotenv()
def create(prompt):
    openai.api_key = os.getenv('OPENAI_API_KEY')

    response = openai.Image.create(
        prompt = prompt,
        n=1,
        size = "512x512"
    )
    image_url = response["data"][0]["url"]
    print(image_url)

create("cat")
