import os
import json
import requests

# Define your OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

# Define the endpoint URL
url = "https://api.openai.com/v1/images/generations"

# Set up the headers, including authorization with your API key
headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

# Define the payload with your desired prompt and other parameters
payload = {
    "prompt": "A futuristic cityscape at dusk with flying cars and neon lights",
    "n": 1,  # Number of images to generate
    "size": "1024x1024",  # Size of the generated image
}

# Send a POST request to the OpenAI API
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check if the request was successful
if response.status_code == 200:
    # Get the image URL from the response
    image_url = response.json()["data"][0]["url"]
    # Fetch the image
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        # Save the image to the current directory
        with open("generated_image.png", "wb") as file:
            file.write(image_response.content)
    else:
        print("Failed to download the image.")
else:
    print("Failed to generate the image.")
