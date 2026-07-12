import json

with open("llm_config.json", "r") as file:
    data = json.load(file)
    print("Model:", data["model"]["name"])
    print("Temperature:", data["model"]["temperature"])
    print("Port:", data["server"]["port"])
    print("Username:", data["users"][0]["username"])
    print("Second User's role:", data["users"][1]["role"])
    print("Logging level:", data["logging"]["level"])
        
data["users"].append({
"username": "alice",
"role": "developer"
})
data["database"] = {
"host": "localhost",
"port": 5432
}
data["model"]["name"] = "gpt-4.1"
data["model"]["temperature"] = 0.2
data["model"]["max_tokens"] = 1024
data["server"]["port"] = 8080
data["logging"]["level"] = "DEBUG"

with open("llm_config.json", "w") as file:
    json.dump(data, file, indent=4)