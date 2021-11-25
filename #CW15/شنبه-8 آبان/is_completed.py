import json

with open("isCompleted.json", "r") as file_reader:
    titles = json.load(file_reader)
    for item in titles:
        if item["completed"]:
            print(item)
