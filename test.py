import requests

url = "https://catfact.ninja/fact"
    
# Doe de API-aanroep
response = requests.get(url)

data = response.json()
cat_fact = data.get("fact")

print("Kattenfeitje: ", cat_fact)