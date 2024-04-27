#!/usr/bin/python3
""" takes your GitHub credentials (username and password) and uses the
    GitHub API to display your id """


import requests
from sys import argv


if __name__ == "__main__":
    username, password = argv[1:]
    authorization = "Bearer {}".format(password)
    url = "https://api.github.com/user"
    header = {'Accept': "application/vnd.github+json",
              'Authorization': authorization,
              'X-GitHub-Api-Version': "2022-11-28"}
    try:
        response = requests.get(url=url,
                                headers=header,
                                auth=(username, password))
        print(response.json().get('id'))
    except requests.exceptions.RequestException as e:
        status_code = response.status_code
        if status_code:
            print("Error code:", status_code)
    except requests.JSONDecodeError as e:
        print("Not a valid JSON", e)
