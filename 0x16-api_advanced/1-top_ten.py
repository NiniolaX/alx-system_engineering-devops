#!/usr/bin/python3
"""
Contains a function that prints the first 10 hot posts listed for a given
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

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': '0x16-api_advanced:project (by dev_niniolax)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            # Extract top 10 posts
            top_ten_posts = data['data']['children'][:10]
            top_ten_titles = [post['data']['title'] for post in top_ten_posts]

            for title in top_ten_titles:
                print(title)
            return
        else:
            print(None)
    except Exception as e:
        print(e)
