 import pandas as pd
import requests
import json

# 1. Load Excel file
excel_file = 'your_file.xlsx'
df = pd.read_excel(excel_file)

# 2. Convert to JSON (optional, depends on API)
data = df.to_dict(orient='records')

# 3. POST to website
url = 'https://example.com/api/upload'  # replace with actual endpoint

# if the API expects raw JSON:
headers = {'Content-Type': 'application/json'}
response = requests.post(url, headers=headers, json=data)

# 4. Save the response to JSON file
output_file = 'response.json'
with open(output_file, 'w') as f:
    json.dump(response.json(), f, indent=2)

print(f"Response saved to {output_file}")
