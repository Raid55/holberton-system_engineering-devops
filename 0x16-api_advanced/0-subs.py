#!/usr/bin/python3
""" 0 - gather data from reddit """
import requests



def number_of_subscribers(subreddit):
    baseUrl = "https://www.reddit.com/r/{}/about.json"

    res = requests.get(baseUrl.format(subreddit), allow_redirects=False).json()
    if "data" in res and "subscribers" in res['data']:
        return res["data"]["subscribers"]
    else:
        return 0
