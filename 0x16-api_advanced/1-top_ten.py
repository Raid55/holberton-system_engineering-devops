#!/usr/bin/python3
""" 1 - gather data from reddit """
import requests



def top_ten(subreddit):
    baseUrl = "https://www.reddit.com/r/{}/hot.json"

    res = requests.get(baseUrl.format(subreddit), allow_redirects=False).json()
    if "data" in res and "children" in res['data']:
        for i in range(0, 10):
            print(res['data']['children'][i]['data']['title'])
    else:
        print(None)
