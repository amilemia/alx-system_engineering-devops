#!/usr/bin/python3
"""
this is doc module
"""
import requests

headers = {"User-Agent": "MyCustomUserAgent/1.0"}

def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively query the Reddit API, parse article titles, and print sorted keyword counts.

    :param subreddit: The name of the subreddit to search.
    :param word_list: A list of keywords to count.
    :param after: The 'after' parameter for pagination (default is None).
    :param counts: A dictionary to store keyword counts (default is None).
    """
    if counts is None:
        counts = {}

    if not subreddit:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    if after:
        url += f"&after={after}"

    response = requests.get(url, allow_redirects=False, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"]:
            title = post["data"]["title"]
            for word in word_list:
                lowercase_title = title.lower()
                lowercase_word = word.lower()
                if f" {lowercase_word} " in f" {lowercase_title} ":
                    counts[lowercase_word] = counts.get(lowercase_word, 0) + 1

        after = data["data"]["after"]
        if after:
            return count_words(subreddit, word_list, after, counts)
    else:
        return
