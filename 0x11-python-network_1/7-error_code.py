#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays the body of
    the response. """


import requests
from sys import argv


url, = argv[1:]
try:
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)
except requests.exceptions.RequestException as e:
    status_code = response.status_code
    if status_code:
        print("Error code:", status_code)
        
