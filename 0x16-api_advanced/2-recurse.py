#!/usr/bin/python3
""" 2 - gather data from reddit """
import requests



def recurse(subreddit, nextPage=None, hotList=[]):
    baseUrl = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if nextPage:
        baseUrl = baseUrl + "?after={}".format(nextPage)

    res = requests.get(baseUrl, allow_redirects=False).json()

    if "data" not in res:
        return None

    if "children" in res['data']:
        for child in res['data']['children']:
            hotList.append(child['data']['title'])
    
    if res['data']['after'] is not None:
        return recurse(subreddit, nextPage=res['data']['after'], hotList=hotList)
    else:
        return hotList
