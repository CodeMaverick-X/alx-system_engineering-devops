#!/usr/bin/python3
"""This module contains a function that quaries the `Reddit API`
and returns the number of subcribers for a given subreddit.
Return: 0 on invalid subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """function to return subcribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
            'User-Agent': 'Reinhard',
            'Accept': 'application/json'
            }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    return 0
