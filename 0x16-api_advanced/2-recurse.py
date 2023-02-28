#!/usr/bin/python3
""" Recurse it!"""
import requests


def recurse(subreddit, hot_list=[], anchor=""):
    """returns a list containing the titles of all hot articles
    for a given subreddit"""

    api = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'by my helper'}
    params = {'limit': 1}
    if anchor != "":
        params['after'] = anchor

    res = requests.get(api, headers=headers, allow_redirects=False,
                       params=params)

    if res.status_code != 200:
        return None

    item = res.json().get('data').get('children')[0]
    title = item.get('data').get('title')
    hot_list.append(title)

    # anchor = item['kind'] + '_' + item['data']['id']
    anchor = res.json().get('data').get('after')

    # print(anchor)
    # print(hot_list)
    if anchor:
        recurse(subreddit, hot_list, anchor)
    else:
        return hot_list
