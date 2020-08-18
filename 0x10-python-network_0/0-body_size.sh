#!/bin/bash
# to get the body size
curl -s $1 | wc -c
