#!/usr/bin/python3
"""
Contains a fuunction that returns the number of subscribers to a given
subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers of a given subreddit """
    if subreddit is None:
        return 0

    try:
        url = f'https://www.reddit.com/r/{subreddit}/about.json'
        headers = {'User-Agent': 'SubscriberCounter/1.0 by dev_niniolax'}
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscriber_count = data.get('data').get('subscribers')
            return subscriber_count
        else:
            return 0
    except Exception as e:
        print('Error fetching subreddit: {}'.format(e))
        return 0
