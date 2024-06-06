#!/usr/bin/python3
"""
Returns a list containing all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list containing the titles of all hot articles for a given
    subreddit.
    Args:
        subreddit(str): Subreddit
        hot_list(list): List of titles
        after(str): Fullname of item to use as starting poiny for next slice
    Return:
        (list of str): List of titles of all hot articles or None on error
    """
    # params = f'limit={limit}&after={after}&count={count}'
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': '0x16-api_advanced:project (by dev_niniolax)'}
    params = {'limit': 100}
    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        # Extract titles
        posts = data['data']['children']
        titles = [post['data']['title'] for post in posts]
        hot_list.extend(titles)
        # Update params
        after = data['data']['after']

        if after:
            # Recursively fetch remaining hot posts
            recurse(subreddit, hot_list, after)
        else:
            # Return list of titles after all hot posts have been fetched
            return hot_list
    else:
        return None
