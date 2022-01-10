#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password) and uses
the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    paswd = sys.argv[2]
    hdrs = {"Accept": "application/vnd.github.v3+json"}
    url = "https://api.github.com/user"
    r = requests.get(url,  auth=(username, paswd), headers=hdrs)
    print(r.json()["id"])
