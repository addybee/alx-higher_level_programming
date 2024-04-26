#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status """


import requests


url = "https://alx-intranet.hbtn.io/status"
response = requests.get(url)
content = response.text
content_type = type(content)
print("Body response:\n    - type: {}\n    - content: {}".format(content_type,
                                                                 content))
