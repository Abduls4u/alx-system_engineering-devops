#!/usr/bin/python3
'''contains a function that queries the Reddit API
Usage:
   ./0-subs.py
Author:
    Abdulsalam Abdulsomad .A. - May 16th, 2023.
'''
import requests


def number_of_subscribers(subreddit):
    '''A  function that queries the Reddit API and returns the
 number of subscribers (not active users, total subscribers) for a
given subreddit
        parameters:
        ***********
            subreddit(str): subreddit to query.
        Return:
        *******
            The number of subscribers.
        Raise:
        ******
             void
    '''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {'User-Agent': 'MyBot/1.0'}
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        return (0)
    else:
        data = response.json()
        subs = data['data']['subscribers']
        return (subs)
