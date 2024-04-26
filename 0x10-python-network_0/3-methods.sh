#!/bin/bash
# that takes in a URL and displays all HTTP methods the server will accept.
curl -I ALLOW $1
