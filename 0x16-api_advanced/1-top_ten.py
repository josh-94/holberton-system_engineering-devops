#!/usr/bin/python3
''' Function that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit. '''

import requests


def top_ten(subreddit):
    ''' protoype function '''
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    head = {"User-Agent": "Josh"}
    request = requests.get(url, headers=head, allow_redirects=False)
    if request.status_code == 200:
        data = request.json().get("data")
        child = data.get("children")
        for data_list in child:
            title = data_list.get("data").get("title")
            print(title)
    else:
        print(None)
