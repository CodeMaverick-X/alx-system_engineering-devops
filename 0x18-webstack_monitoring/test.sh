#!/usr/bin/env bash
curl -X GET "https://api.datadoghq.com/api/v1/hosts" \
	-H "Accept: application/json" \
	-H "DD-API-KEY: 2f06764286934d2f1624745adcd03b36" \
	-H "DD-APPLICATION-KEY: 28cbe174ce5546e712fd66ce44a80fd56536cedd"
