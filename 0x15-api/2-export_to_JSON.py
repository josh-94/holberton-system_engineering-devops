#!/usr/bin/python3
'''Python script to export data in the JSON format.'''
import json
import requests
from sys import argv


def R_API():
    # Validate if argument has index and is an interger
    try:
        employeeID = int(argv[1])

    except ValueError:
        print('Value Error')
        exit()
    except IndexError:
        print('Index Error')
        exit()

    # Python requets get method'''
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(employeeID))
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(employeeID))
    user_name = user.json().get('username')
    # Getting variables
    datafile = {}
    datafile[employeeID] = []

    # Export data in JSON format
    with open("{}.json".format(employeeID), "w") as jsonfile:
        for data in todo.json():
            task_title = data.get("title")
            task_completed_s = data.get("completed")
            datafile[employeeID].append({
                "task": task_title,
                "completed": task_completed_s,
                "username": user_name,
            })
        json.dump(datafile, jsonfile)


if __name__ == "__main__":
    R_API()
