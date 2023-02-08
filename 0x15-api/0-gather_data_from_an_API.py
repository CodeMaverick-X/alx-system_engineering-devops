#!/usr/bin/python3
"""
this script returns info of an employees to do list
using the rest api
"""

import requests
from sys import argv

id = argv[1]
url1 = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
url2 = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

res_todo = requests.get(url1)
res_user = requests.get(url2)

todo = res_todo.json()
user = res_user.json()

done = 0
total = 0
for i in todo:
    total = total + 1
    if i['completed']:
        done = done + 1

print('Employee {} is done\
 with tasks({}/{}):'.format(user['name'], done, total))

for j in todo:
    if j['completed']:
        print('     {}'.format(j['title']))
