#!/usr/bin/python3
"""Module that has a recursive function that
queries the Reddit API and returns a list containing the
titles of all hot articles
for a given subreddit"""
import requests


'''after: A parameter used for pagination to fetch the next set of results. '''
'''after Key Value: A string that is the ID of
the last post in the current batch of results.'''
def recurse(subreddit, hot_list=[], after=None):
    ''' a function that queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit'''
    base_url = "https://www.reddit.com/r/"
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    if after is not None:
        url = f"{base_url}/r/{subreddit}/hot.json?after={after}"
    else:
        url = f"{base_url}/r/{subreddit}/hot.json"

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        '''{}: degault to be returned'''
        '''data: key in the dictionary returned as json'''
        data = response.json().get('data', {})
        children = data.get('children', [])

        for post in children:
            ''' data has children key and children has a data key'''
            hot_list.append(post['data']['title'])

        after = data.get('after')

        if after:
            # Recursive call with updated 'after'
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
