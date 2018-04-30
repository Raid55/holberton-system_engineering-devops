#!/usr/bin/python3
""" 3 - export all users to json """
import requests
import json
import csv


def main():
    """ does api request to get info and exports it"""

    baseUrl = "https://jsonplaceholder.typicode.com/"
    retDict = {}

    users = requests.get(baseUrl + "users").json()

    for user in users:
        todos = requests.get(baseUrl + "todos?userId={}".format(
            user['id']
        )).json()
        retDict[user['id']] = [{
                "username": user['name'],
                "task": todo['title'],
                "completed": todo['completed']
            } for todo in todos
        ]

    with open('todo_all_employees.json'.format(id), 'w+') as f:
        json.dump(retDict, f)


if __name__ == "__main__":
    main()
