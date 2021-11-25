# import json
#
# data = {
#     "president": {
#         "name": "Zaphod Beeblebrox",
#         "species": "Betelgeusian"
#     },
#     "number": None,
#     "went_uni": True,
#     "married": False
# }
#
# with open("my_data.json", "w") as file_writer:
#     json.dump(data, file_writer, indent=4)

# import json
#
# data = {
#     "president": {
#         "name": "Zaphod Beeblebrox",
#         "species": "Betelgeusian"
#     }
# }
#
# with open("das.json", "w") as file_writer:
#     json.dumps(data)

# import json
#
# blackjack_hand = (8, "Q")
# encode = json.dumps(blackjack_hand)
# decode = json.loads(encode)
# print(blackjack_hand == decode)
# print(type(encode))
# print(encode)
# print(type(decode))
# print(decode)
# print(tuple(decode) == blackjack_hand)

# import json
#
# with open("person_data.json", "r") as file_reader:
#     person = json.load(file_reader)
#     print(person)

# import json
#
# json_string = """
# {
#     "researcher": {
#         "name": "Ford Prefect",
#         "species": "Betelgeusian",
#         "relatives": [
#             {
#                 "name": "Zaphod Beeblebrox",
#                 "species": "Betelgeusian"
#             }
#         ]
#     }
# }
# """
# json_json = json.loads(json_string)
# print(json_json)

# import json
#
# with open("MOCK_DATA.json", "r") as file_reader:
#     file_data = json.load(file_reader)
#     print(file_data[2])


