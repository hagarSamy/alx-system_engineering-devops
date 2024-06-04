#!/usr/bin/python3
"""Module that has a recursive function that
queries the Reddit APIparses the title of all hot articles,
and prints a sorted count of
given keywords (case-insensitive, delimited by spaces"""
import requests


def count_words(subreddit, word_list, counts={}, after=None):
    ''' a function that queries queries the Reddit API and returns a list
    containing the titles of all hot articles for a
    given subreddit. If no results are
    found for the given subreddit, the function should return None.'''
    base_url = "https://www.reddit.com/r"
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    if after is not None:
        url = f"{base_url}/{subreddit}/hot.json?after={after}"
    else:
        url = f"{base_url}/{subreddit}/hot.json"
        word_list = [word.lower() for word in word_list]
        '''count for each word initialized to'''
        counts = {word: 0 for word in word_list}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        '''{}: degault to be returned'''
        '''data: key in the dictionary returned as json'''
        data = response.json().get('data', {})
        children = data.get('children', [])

        for post in children:
            ''' data has children key and children has a data key'''
            hot_list = post['data']['title']
            split_words = hot_list.split()
            split_words = [word.lower() for word in split_words]
            for word in word_list:
                counts[word] += split_words.count(word)

        after = data.get('after')

        if after:
            # Recursive call with updated 'after'
            return count_words(subreddit, word_list, counts, after)
        else:
            '''sorts according to values returned from .items
            -- key and lambda part'''
            '''.items returns a list of tuples of ks, vs'''
            '''lambda processes on each element of the iteratable(2nd arg)'''
            '''reverse=True: This argument sorts the list in
            descending order.'''
            sorted_counts = dict(sorted(counts.items(),
                                        key=lambda item: item[1],
                                        reverse=True))
            for key, value in sorted_counts.items():
                if value > 0:
                    print(f"{key}: {value}")
            return counts
    else:
        return None
