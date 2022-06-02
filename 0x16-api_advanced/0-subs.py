#!/usr/bin/python3
''' Function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0. '''

import requests


def number_of_subscribers(subreddit):
    ''' protoype function '''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    head = {"User-Agent": "Josh"}
    request = requests.get(url, headers=head, allow_redirects=False).json()
    data = request.get("data", {})
    subs = data.get("subscribers", 0)
    return subs
