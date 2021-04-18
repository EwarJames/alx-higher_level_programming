#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the response.

Usage: ./3-error_code.py <URL>
"""
import sys
import urllib.request
import urllib.error


__name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode(ascii))
    except urllib.error.HTTPerror as e:
        print("Error code: {}".format(e.code))
