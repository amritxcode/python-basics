import requests

url = "https://jsonplaceholder.typicode.com/posts"

student = {
    "name": "Amrit",
    "college": "Sri Sri University",
    "course": "CSE AIML"
}

response = requests.post(url, json=student)

print(response.status_code)
print(response.json())