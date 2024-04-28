#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


import sys
import requests


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        value = {"q": sys.argv[1]}
    else:
        value = {"q": ""}
    r = requests.post(url, data=value)
    try:
        json_response = r.json()
        if json_response:
            # Display id and name if JSON is not empty
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            # Display "No result" if JSON is empty
            print("No result")
    except ValueError:
        # Display "Not a valid JSON" if JSON is invalid
        print("Not a valid JSON")
