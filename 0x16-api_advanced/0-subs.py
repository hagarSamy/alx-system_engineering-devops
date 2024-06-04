#!/usr/bin/python3
# a function that queries the Reddit API and returns the number of subscribers
# Invalid subreddits may return a redirect to search results.
import requests


def number_of_subscribers(subreddit):
    # r: stands for subredirect in the construct
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Set the custom User-Agent to avoid Too Many Requests errors
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko)\
        Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    return 0
