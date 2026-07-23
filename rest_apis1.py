import requests

url = "https://randomuser.me/api/"

response = requests.get(url)

data = response.json()
print(response.status_code)
print(data)

first_name= (data["results"][0]["name"]["first"])
print(f"First name: {first_name}")
print(f"Email: {data['results'][0]['email']}")
print(f"Country: {data['results'][0]['location']['country']}")