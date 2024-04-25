#!/bin/bash
#  takes in a URL and displays all HTTP methods the server will accept.
curl -Is -X OPTIONS $1 | awk 'BEGIN { RS="\n" } /Allow:/ { line=$2; for (i=3; i<=NF; i++) line = line " " $i; print line }'
