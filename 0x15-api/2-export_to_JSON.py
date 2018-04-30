#!/usr/bin/python3
""" 2 - export to json """
from sys import argv
import requests
import json
import csv


def main(id):
    """ does api request to get info and exports it"""
    
    baseUrl = "https://jsonplaceholder.typicode.com/"

    user = requests.get(baseUrl + "users/{}".format(id)).json()
    todos = requests.get(baseUrl + "todos?userId={}".format(id)).json()

    with open('{}.json'.format(id), 'w+') as f:
        json.dump({
            id: [{
                    "task": todo['title'], 
                    "completed": todo['completed'],
                    "username": user['name']
                } for todo in todos
            ]
        }, f)
    

if __name__ == "__main__":
    main(argv[1])

