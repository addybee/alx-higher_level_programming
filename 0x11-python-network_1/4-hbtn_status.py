#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status """


import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.text
    content_type = type(content)
    print("Body response:\n\t- type: {}\n\t- content: {}".
          format(content_type, content))
