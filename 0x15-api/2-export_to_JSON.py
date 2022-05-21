#!/usr/bin/python3
'''Script that, using an REST API, for a given employee ID,
returns information about his/her TODO list progress.'''
import json
import requests
from sys import argv


def R_API():
    # Validate if argument has index and is an interger
    try:
        employee_id = int(argv[1])

    except ValueError:
        print('Value Error')
        exit()
    except IndexError:
        print('Index Error')
        exit()

    # Python requets get method'''
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(employee_id))
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(employee_id))
    user_name = user.json().get('username')
    # Getting variables
    data = {}
    data[employee_id] = []

    with open("{}.json".format(employee_id), 'w') as jsonfile:
        for data_f in todo.json():
            task_completed_s = data_f.get('completed')
            task_title = data_f.get('title')
            data[employee_id].append({
                "task": task_title,
                "completed": task_completed_s,
                "username": user_name,
            })
            json.dump(data, jsonfile)


if __name__ == "__main__":
    R_API()
