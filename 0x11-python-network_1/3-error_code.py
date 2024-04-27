#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays the body of
    the response (decoded in utf-8)."""


from urllib import request, error
from sys import argv


if __name__ == "__main__":
    url, = argv[1:]
    print(url)
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            print(content)
    except error.HTTPError as e:
        print('Error code:', e.code)
