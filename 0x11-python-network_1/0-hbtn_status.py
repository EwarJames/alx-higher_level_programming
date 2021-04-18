#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status url."""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        bdy = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(bdy)))
        print("\t- content: {}".format(bdy))
        print("\t- utf8 content: {}".format(bdy.decode("utf-8")))
