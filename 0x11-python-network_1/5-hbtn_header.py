#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays the value of
    the variable X-Request-Id in the response header"""


import requests
from sys import argv


url, = argv[1:]
response = requests.get(url)
X_Request_Id = response.headers.get('X-Request-Id')
print(X_Request_Id)
