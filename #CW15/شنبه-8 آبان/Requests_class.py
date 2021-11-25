# import requests
#
# response = requests.get('https://api.github.com')
# print(response.text)

# import requests
#
#
# def request_to_random_user():
#     response = requests.get("https://randomuser.me/api/")
#     print(response)
#
#
# request_to_random_user()

# import json
# import requests
# from pprint import pprint
#
#
# def random_user_request():
#     response = requests.get("https://randomuser.me/api/")
#     json_data = json.loads(response.text)
#     pprint(json_data)
#
#
# random_user_request()

# import requests
#
#
# def random_user():
#     response = requests.get("https://randomuser.me/api/")
#     print(response.json())
#
#
# random_user()

# import requests
#
#
# def random_user():
#     response = requests.get("https://randomuser.me/api/", params={"q": "django"})
#     data = response.json()
#     print(data["results"][0]["location"]["street"])
#
#
# random_user()

import requests
from requests.exceptions import HTTPError


def random_user():
    try:
        response = requests.get("https://api.github.com/search/commits", params={"qaaaaaaa": "django"})
        response.raise_for_status()
    except HTTPError as he:
        print(he)
    print(response.json())


random_user()

# import requests
# from requests.exceptions import HTTPError
#
#
# def req_to_github_search():
#     try:
#         response = requests.get('https://api.github.com/search/commits',
#                                 params={'qaaaaa': 'django'})
#         response.raise_for_status()
#     except HTTPError as he:
#         print("the http error is :", he)
#     # print(response.json())
#
#     data = response.json()
#     # print(data['items'][2]['author']['avatar_url'])
#
# req_to_github_search()
