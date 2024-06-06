#!/usr/bin/python3
"""
Contains a fuunction that returns the number of subscribers to a given
subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers of a given subreddit """
    if subreddit is None or type(subreddit) is not str:
        return 0

    try:
        url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
        headers = {'User-Agent': '0x16-api_advanced:project (by dev_niniolax)'}
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            subreddit_data = response.json().get('data')
            subscriber_count = subreddit_data.get('subscribers')
            return subscriber_count
        else:
            return 0
    except Exception as e:
        print('Error fetching subreddit: {}'.format(e))
        return 0
