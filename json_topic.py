import json

with open("config.json") as file:
    data = json.load(file)
    print(data)
    print(type(data))

    data["model"] = "gpt-4.1"
    data["temperature"] = 0.3
    data["is_finetuned"] = False
    data["allowed_users"].append("amrit_ray")

with open("config.json", "w") as file:
    json.dump(data, file, indent=4)
