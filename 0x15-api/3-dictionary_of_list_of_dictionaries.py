#!/usr/bin/python3
'''Python script to export data in the JSON format.'''
import json
import requests
from sys import argv


def R_API():
    '''Getting data from REST API'''

    # Python requets get method
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()

    datafile = {}
    for user in users:
        obj = []
        for task in todos:
            if task.get("userId") == user.get("id"):
                var = {'username': user.get("username"),
                       'task': task.get("title"),
                       'completed': task.get("completed"),
                       }
                obj.append(var)
        datafile[str(user.get("id"))] = obj
        with open('todo_all_employees.json', 'w') as file:
            json.dump(datafile, file)


if __name__ == "__main__":
    R_API()
