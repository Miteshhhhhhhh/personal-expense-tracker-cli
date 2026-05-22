#Learning requests
#retrying


import requests
from requests.exceptions import Timeout
# base_url = "https://pokeapi.co/api/v2/"
# Max_retries = 3
#
# for i in range(Max_retries):
#     try:
#         r = requests.get(base_url, timeout=0.2)
#         print(r.text)
#         print(r.status_code)
#         break
#     except:
#         print("Timeout")
# else:
#     print("All retries failed")
#
#
# import requests
# import config
#
# # r = requests.get(config.users())
# # print(r.text) #if we want data in string form
# # print(r.json()) #if we want data in dict/list form
#
# url = requests.get(config.users())
# name = input("Enter the name:")
# Email = input("Enter the Email:")
# Status = input("Enter the Status:")
# Gender = input("Enter the gender:")
#
# details = {
#     "name" : name,
#     "email" : Email,
#     "status" : Status,
#     "gender" : Gender
# }
#
# print(requests.post(url, data=details))
import  requests
import config

url = config.users()
token = config.access_token()

headers = {
    "Authoraization" : f"Bearer {token}",
    "Accept" : "application/json"
}
r = requests.get(url, headers = headers)
print(r.status_code)
print(r.text)