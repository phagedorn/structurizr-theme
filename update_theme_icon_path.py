import json

# Load the JSON data
with open('theme.json', 'r') as file:
    data = json.load(file)

# Define the base URL to be added
base_url = "https://github.com/phagedorn/structurizr-theme/blob/main/icons/"

# Update the icon paths with the base URL
for element in data.get("elements", []):
    if "icon" in element:
        element["icon"] = base_url + element["icon"]

# Save the updated JSON back to the file
with open('theme_updated.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Updated theme.json successfully.")
