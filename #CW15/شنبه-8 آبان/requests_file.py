# import requests
#
# sample_request = requests.get("https://api.github.com")
# print(sample_request)
# print(sample_request.status_code)

# import requests
#
# sample_request = requests.get("https://api.github.com/authorizations")
# if sample_request.status_code == 200:
#     print("OK")
# elif sample_request.status_code == 404:
#     print("NOT FOUND")
# else:
#     print("ELSE")

# import requests
#
# response = requests.get("https://api.github.com/authorizations")
# if response:
#     print("OK")
# else:
#     print("NOT FOUND")

# import requests
# from requests.exceptions import HTTPError
#
# for url in ['https://api.github.com', 'https://api.github.com/invalid']:
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#
#     except HTTPError as http_err:
#         print(f'HTTP error occurred: {http_err}')
#
#     except Exception as err:
#         print(f'Other error occurred: {err}')
#
#     else:
#         print('Success!')

# import requests
#
# response = requests.get("https://api.github.com")
# print(response.content)

# import requests
#
# response = requests.get("https://api.github.com")
# print(response.text)

# import requests
#
# response = requests.get("https://api.github.com")
# print(response.json())
