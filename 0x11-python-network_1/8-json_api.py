#!/usr/bin/python3
""" takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter. """


import requests
from sys import argv


if __name__ == "__main__":
    p = ""
    if len(argv) > 1:
        p = argv[1]
    try:
        url = "http://0.0.0.0:5000/search_user"
        response = requests.post(url, data={'q': p})
        response.raise_for_status()
        if response.headers.get("Content-Type") == "application/json":
            content = response.json()
            if len(content) < 1:
                print("No result")
            else:
                print("[{}] {}".format(content.get("id"), content.get("name")))
        else:
            print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        status_code = response.status_code
        if status_code:
            print("Error code:", status_code)
