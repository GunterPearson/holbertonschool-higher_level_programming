#!/bin/bash
# all it accepts
curl -sI $1 | grep "Allow" | sed 's/Allow: //'
