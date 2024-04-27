#!/usr/bin/python3
"""
that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""


import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            body = response.read().decode("ascii")
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
