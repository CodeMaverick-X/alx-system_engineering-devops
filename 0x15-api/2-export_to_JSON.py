#!/usr/bin/python3
"""Return info of an employees to do list
using the rest api in json format.
"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    id = argv[1]
    url1 = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    url2 = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

    res_todo = requests.get(url1)
    res_user = requests.get(url2)

    todo = res_todo.json()
    user = res_user.json()

    with open('{}.json'.format(id), 'w') as f:
        new = []
        k = {}
        for j in todo:
            k.update({"task": j['title']})
            k.update({"completed": j['completed']})
            k.update({"username": user['username']})
            new.append(k)
        dic = json.dumps({id: new})
        f.write(dic)
