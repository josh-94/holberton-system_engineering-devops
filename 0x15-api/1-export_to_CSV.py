#!/usr/bin/python3
'''Extend your Python script to export data in the CSV format.'''
import csv
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
    todo = requests.get('https://jsonplaceholder.typicode.com/todos')
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(employee_id))

    user_name = user.json().get('username')

    # Open the file in the write mode with format specified
    with open("{}.csv".format(employee_id), 'w') as f:

        # Create the csv writer
        writer = csv.writer(f)

    for data in todo.json():
        task_completed_s = data.get('completed')
        task_title = data.get('title')
        print('"{}","{}","{}","{}"'
              .format(employee_id, user_name, task_completed_s, task_title))


if __name__ == "__main__":
    R_API()
