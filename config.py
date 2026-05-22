#TO STORE DIFFERENT VALUES FOR API.
import os

Base_URL = "https://gorest.co.in" #Domain URL
Base_path = "/public/"
VERSION = "v2/"
USER = "users"

def users():
    return Base_URL + Base_path + VERSION + USER

def access_token():
    return os.getenv("TEST_TOKEN")



#Practice 2

