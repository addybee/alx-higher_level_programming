#!/usr/bin/python3
""" takes 2 arguments in order to solve a challenge. """


import requests
from sys import argv


if __name__ == "__main__":
    repo_name, owner_name = argv[1:]
    header = {'Accept': "application/vnd.github+json",
              'X-GitHub-Api-Version': "2022-11-28"}
    url = "https://api.github.com/repos/{}/{}/commits".format(owner_name,
                                                              repo_name)
    try:
        response = requests.get(url, headers=header)
        content = response.json()
        for i in range(10):
            print("{}: {}".format(content[i].get('sha'),
                  content[i].get('commit').get('author').get('name')))
    except Exception:
        pass
