import json
import requests
import os

# Define the base URL and the path to save the images
base_url = "https://static.structurizr.com/themes/microsoft-azure-2023.01.24/"
output_dir = "./"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to download an image from a given URL
def download_image(image_name):
    url = base_url + image_name
    response = requests.get(url)
    if response.status_code == 200:
        file_path = os.path.join(output_dir, image_name)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {image_name}")
    else:
        print(f"Failed to download: {image_name}")

# Read the JSON file from the URL
json_url = "https://static.structurizr.com/themes/microsoft-azure-2023.01.24/theme.json"
response = requests.get(json_url)
if response.status_code == 200:
    theme_data = response.json()
    
    # Extract the "icon" values and download the images
    for element in theme_data.get("elements", []):
        if "icon" in element:
            icon_name = element["icon"]
            download_image(icon_name)
else:
    print(f"Failed to fetch JSON from {json_url}")
