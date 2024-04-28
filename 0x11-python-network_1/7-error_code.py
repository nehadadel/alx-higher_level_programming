#!/usr/bin/python3
"""
that takes in a URL, sends a request to the URL
and displays the body of the response.
"""


import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.post(url)
    try:
        print(r.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(r.status_code)
