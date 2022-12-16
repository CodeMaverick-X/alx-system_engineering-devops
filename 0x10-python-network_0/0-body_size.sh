#!/bin/bash

text=$(curl -s -I $1 | grep Content-Length)
IFS=' '
read -a strarr <<< "$text"
echo ${strarr[1]}
