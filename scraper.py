import requests
import json
import csv

# URL for Property Count Data
property_count_url = "https://www.magicbricks.com/mbutility/getPropertyCountGroup?cityCode=3327"

# Set Headers
headers = {"User-Agent": "Mozilla/5.0"}

# Fetch Data
response = requests.get(property_count_url, headers=headers)

# Ensure response is JSON
try:
    property_data = json.loads(response.text)
except json.JSONDecodeError:
    print("❌ Error: Response is not valid JSON.")
    exit()

# Extract 'propCount' dictionary
if "propCount" in property_data:
    property_counts = property_data["propCount"]  # This is now a dictionary
else:
    print("❌ Error: 'propCount' key not found in API response.")
    exit()

# Convert dictionary to a list of dictionaries
property_list = [{"businessType": key, "propertyCount": value} for key, value in property_counts.items()]

# Save to CSV
csv_filename = "property_counts.csv"
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["S.No", "Business Type", "Property Count"])  # Header

    for idx, item in enumerate(property_list, start=1):
        writer.writerow([idx, item["businessType"], item["propertyCount"]])

print(f"✅ Property data saved to {csv_filename}")
