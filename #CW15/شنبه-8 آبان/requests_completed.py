import requests


response = requests.get("https://jsonplaceholder.typicode.com/todos")
data = response.json()

users = {}

for d in data:
    if d["completed"]:
        if d["userId"] not in users.keys():
            users[d["userId"]] = 1
        else:
            users[d["userId"]] += 1

print(sorted(users.items(), key=lambda x: x[1], reverse=True))
