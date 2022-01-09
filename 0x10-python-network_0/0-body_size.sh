#!/usr/bin/bash
# takes in an url and sends a request to that url and display size of body reference
curl -Is "$1" | grep Content-Length | cut -d ' ' -f2
