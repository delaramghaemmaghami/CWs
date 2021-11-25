# import json
# import pprint
#
# my_data_str = """{
#     "myName": "Raha",
#     "myLastName": "Parsa",
#     "hobbies": [null, "blogging", "programming"],
#     "test" : null,
#     "age": 25,
#     "languages": [
#                     {
#                         "name": "python",
#                         "years": 2.5
#                         },
#                     {
#                         "name": "R",
#                         "years": 2
#                         },
#                     {
#                         "name": "C++",
#                         "years": 1
#                         },
#                     {
#                     "name": "Java",
#                     "years": 1
#                     }
#                 ]
#             }"""
# data_str = json.loads(my_data_str)
# print(data_str)
# pprint.pprint(data_str)
# print(type(data_str))

# import json
#
# my_data = {
#     "myName": "رها",
#     "myLastName": "پارسا",
#     "hobbies": [None, "blogging", "programming"],
#     "age": 25,
#     "test": None,
#     "languages": [
#         {
#             "name": "python",
#             "years": 2.5
#         },
#         {
#             "name": "R",
#             "years": 2
#         },
#         {
#             "name": "C++",
#             "years": 1
#         },
#         {
#             "name": "Java",
#             "years": 1
#         }
#     ]
# }
#
# with open("my_data.json", "w") as file_writer:
#     json.dump(my_data, file_writer, indent=4)
