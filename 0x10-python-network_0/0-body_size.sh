#!/bin/bash
# A Bash script that sends URL
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
