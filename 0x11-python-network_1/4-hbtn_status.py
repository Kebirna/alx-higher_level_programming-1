#!/usr/bin/python3

"""
 script that fetches https://intranet.hbtn.io/status
"""

import requests

if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
    req = requests.get(url)
    print('Body response:')
    print(f'\t- type: {type(req.text)}')
    print(f'\t- content: {req.text}')

