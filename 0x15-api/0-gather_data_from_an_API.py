#!/usr/bin/python3
""" 0 - gather data from api """
from sys import argv
import requests


def count_completed(taskList):
    return [task for task in taskList if task['completed'] is True]

def main(id):
    """ does api request to get info and print it"""
    
    baseUrl = "https://jsonplaceholder.typicode.com/"

    user = requests.get(baseUrl + "users/{}".format(id)).json()
    todo = requests.get(baseUrl + "todos?userId={}".format(id)).json()

    filteredTodo = count_completed(todo)
    tCount = [len(filteredTodo), len(todo)]

    print("Employee {0} is done with tasks({1}/{2}):".format(user['name'], tCount[0], tCount[1]))

    for todo in filteredTodo:
        print("\t {}".format(todo['title']))


if __name__ == "__main__":
    main(argv[1])
