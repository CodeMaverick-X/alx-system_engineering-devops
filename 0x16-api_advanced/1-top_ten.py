#!/usr/bin/python3
"""This module contains a function that queries
the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """function ints the titles of the first
    10 hot posts listed for a given subreddit."""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
            'User-Agent': 'Reinhard',
            'Accept': 'application/json'
            }
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params={'limit': '10'})

    if response.status_code == 200:
        children = response.json().get('data').get('children')
        for items in children:
            print(items.get('data').get('title'))
    else:
        return print(None)
