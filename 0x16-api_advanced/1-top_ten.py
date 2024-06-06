#!/usr/bin/python3
"""
Contains a function that returns the first 10 hot posts listed for a given
subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the first 10 hot posts listed for a given subreddit.
    Args:
        subreiddit(str): Subreddit
    Return:
        None
    """
    if subreddit is None or type(subreddit) is not str:
        print(None)
        return

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced:project (by dev_niniolax)'}

    try:
        response = requests.get(url, headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            top_ten = data['data']['children']
            for item in top_ten:
                print(item['data']['title'])
            return
        else:
            print(None)
    except Exception as e:
        print(e)
