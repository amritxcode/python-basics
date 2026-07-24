import requests

url ="https://jsonplaceholder.typicode.com/posts"

employee = {
    "name" : "Amrit Ray",
    "salary" : 3000000,
    "profession" : "AI Engineer",
}
response = requests.post(url, json=employee)

print(response.status_code)
print(response.json())