#!/usr/bin/python3
"""Module that has a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    ''' a function that queries the Reddit API and prints the titles
    of the first 10 hot posts'''
    url = "https://www.reddit.com/r/{}/.json?sort='top'&limit=10".format(subreddit)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        ''' children: a key that contains a list of posts or comments'''
        data = response.json()['data']['children']
        for post in data[0:10]:
            print(post['data']['title'])
    else:
        print(None)
