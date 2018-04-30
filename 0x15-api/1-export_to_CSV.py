#!/usr/bin/python3
""" 1 - export to cvs """
from sys import argv
import requests
import csv


def main(id):
    """ does api request to get info and exports it"""
    
    baseUrl = "https://jsonplaceholder.typicode.com/"

    user = requests.get(baseUrl + "users/{}".format(id)).json()
    todos = requests.get(baseUrl + "todos?userId={}".format(id)).json()

    with open('{}.csv'.format(id), 'w+') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos:
            wr.writerow([id, user['name'], todo['completed'], todo['title']])
    

if __name__ == "__main__":
    main(argv[1])
