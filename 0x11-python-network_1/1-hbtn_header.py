#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays the value of the
    X-Request-Id variable found in the header of the response."""


from urllib import request, error
from sys import argv


if __name__ == "__main__":
    url, = argv[1:]

    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            X_Request_Id = response.headers.get('X-Request-Id')
            print(X_Request_Id)
    except error.URLError as e:
        pass
