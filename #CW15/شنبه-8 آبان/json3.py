# import json
#
# with open("person.json", "r") as file_reader:
#     person_data = json.load(file_reader)
#     for item in person_data:
#         print(item)

# import json
#
# data = '{"name": "Bob", "languages": "English"}'
# data_json = json.loads(data)
# print(data_json)
# print(type(data_json))

# import json
#
# data = {"name": "John",
#         "age": 31,
#         "Salary": 25000}
# data_dump = json.dumps(data)
# print(data_dump)
# print(type(data_dump))

# import json
#
# print(json.dumps(['Welcome', "to", "GeeksforGeeks"]))
# print(json.dumps(("Welcome", "to", "GeeksforGeeks")))
# print(json.dumps("Delaram"))
# print(json.dumps(1997))
# print(json.dumps(12.05))
# print(json.dumps(True))
# print(json.dumps(None))

# import json
#
# var = {
#     "Subjects": {
#         "Maths": 85,
#         "Physics": 90
#     }
# }
# with open("Sample.json", "w") as file_writer:
#     json.dump(var, file_writer, indent=4)

# import json
#
# with open("Sample.json", "r") as file_reader:
#     sample_data = json.load(file_reader)
#     print(sample_data)

# import json
#
# json_var = """
# {
#     "Country": {
#         "name": "INDIA",
#         "Languages_spoken": [
#             {
#                 "names": ["Hindi", "English", "Bengali", "Telugu"]
#             }
#         ]
#     }
# }
# """
# json_var_data = json.loads(json_var)
# print(json_var_data)

# import json
#
# employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'
# employee_data = json.loads(employee)
# print(employee_data["name"])
# print(type(employee_data))

# import json
#
# with open("name_language.json", "r") as file_reader:
#     reader = json.load(file_reader)
#     print(reader)

# import json
#
# dictionary = {
#     "name": "sathiyajith",
#     "rollno": 56,
#     "cgpa": 8.6,
#     "phonenumber": "9976770500"
# }
#
# with open("sampl.json", "w") as file_writer:
#     json.dump(dictionary, file_writer, indent=4)

# import json
#
# with open("sampl.json", "a") as file_appender:
#     json.dump(dictionary, file_appender, indent=4)

# import json
#
# person = '{"name": "Bob", "languages": ["English", "Fench"]}'
# person_data = json.loads(person)
# print(person_data)
# print(person_data["languages"])
