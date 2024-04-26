#!/usr/bin/python3
""" takes in a URL and an email address, sends a POST request to the passed
    URL with the email as a parameter, and finally displays the body of the
    response."""


import requests
from sys import argv


url, email = argv[1:]
response = requests.post(url, data={'email': email})
print(response.text)
