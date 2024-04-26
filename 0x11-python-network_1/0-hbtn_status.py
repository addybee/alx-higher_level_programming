#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status """


from urllib import request, error


if __name__ == "__main__":
    req = request.Request("https://alx-intranet.hbtn.io/status")
    try:
        with request.urlopen(req) as response:
            content = response.read()
            content_type = type(content)
            content_utf8 = content.decode('utf-8')
            print("Body response:\n    - type: {}\n    - content: {}\n    - utf8 \
    content: {}".format(content_type, content, content_utf8))
    except error.URLError as e:
        pass
