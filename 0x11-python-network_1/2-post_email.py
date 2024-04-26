#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request to the passed URL with
    the email as a parameter, and displays the body of the response
    (decoded in utf-8) """


from urllib import request, error, parse
from sys import argv


if __name__ == "__main__":
    url, email = argv[1:]

    val = {'email': email}
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = parse.urlencode(val)
    data = data.encode('ascii')
    req = request.Request(url, data, header)
    try:
        with request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            print(content)
    except error.URLError as e:
        pass
