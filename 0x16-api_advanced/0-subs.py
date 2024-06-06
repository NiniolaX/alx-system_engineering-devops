#!/usr/bin/python3
"""
Contains a function that returns the number of subscribers to a given
subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers of a given subreddit.
    Args:
        subreddit(str): Subreddit
    Return:
        (int): Number of subscribers to subreddit or 0 on fail.
    """
    if subreddit is None or type(subreddit) is not str:
        return 0

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': '0x16-api_advanced:project (by dev_niniolax)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscriber_count = data['data']['subscribers']
            return subscriber_count
        else:
            return 0
    except Exception as e:
        # print('Error fetching subreddit: {}'.format(e))
        return 0
