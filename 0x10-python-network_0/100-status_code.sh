#!/bin/bash
# only returns status
curl -s -o /dev/null -w "%{http_code}" "$1"
