#!/usr/bin/python3
"""Return info of an employees to do list
using the rest api in csv format.
"""
import csv
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

    with open('{}.csv'.format(id), 'w') as f:
        writer = csv.writer(f, delimiter=",", quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for j in todo:
            data = [user['id'], user['username'], j['completed'],
                    j['title']]
            writer.writerow(data)
