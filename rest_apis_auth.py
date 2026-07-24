import requests

url = "https://api.example.com/data"

headers = {
    "Authorization": "Bearer abc123xyz"
}

response = requests.get(
    url,
    headers=headers
)