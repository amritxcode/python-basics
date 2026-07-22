import requests

url = "https://api.github.com/users/octocat"

response = requests.get(url)

print(response)
print(response.status_code)

data = response.json()
print(type(data))

print(data["name"])
print(data["followers"])
print(data["following"])
print(data["public_repos"])
print(data["created_at"])



url = "https://api.github.com/users/amritxcode"

response = requests.get(url)

data = response.json()

print(data["name"])
print(data["bio"])
print(data["public_repos"])
print(data["followers"])
print(data["following"])
print(data.get("xyz", "Not Found"))



url =("https://dog.ceo/api/breeds/image/random")

response = requests.get(url)

data = response.json()
print(response.status_code)
print(data.get("message", "Not Found"))
print(data.get("status", "Not Found"))


url = "https://api.agify.io/?name=amrit"
response = requests.get(url)
data = response.json()
print(response.status_code)
print(data)
print(data["name"])
print(data["age"])
print(data["count"])



url = "https://openlibrary.org/search.json?q=python"
response = requests.get(url)
data = response.json()
print(response.status_code)
for book in data["docs"][:5]:
    print(book["title"])