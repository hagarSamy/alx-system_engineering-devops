#!/usr/bin/python3
# a function that queries the Reddit API and returns the number of subscribers
# Invalid subreddits may return a redirect to search results.
import requests


def number_of_subscribers(subreddit):
    # r: stands for subredirect in the construct
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    try:
        response = requests.get(url, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        elif response.status_code in [301, 302, 404]:
            # Handle redirects and not found errors
            return 0
    except Exception:
        return 0
