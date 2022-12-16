#!/bin/bash

text=$(curl -s -I 0.0.0.0:5000 | grep Content-Length)
IFS=' '
read -a strarr <<< "$text"
echo ${strarr[1]}
