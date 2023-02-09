#!/usr/bin/python3
"""Return info of an employees to do list
using the rest api
"""
import requests
from sys import argv
import csv


id = argv[1]
url1 = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
url2 = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

res_todo = requests.get(url1)
res_user = requests.get(url2)

todo = res_todo.json()
user = res_user.json()


with open('{}.csv'.format(id), 'w') as f:
    writer = csv.writer(f)
    for j in todo:
        todo_com_l = []
        todo_com_l.append(user['id'])
        todo_com_l.append(user['name'])
        todo_com_l.append(j['completed'])
        todo_com_l.append(j['title'])
        writer.writerow(todo_com_l)
