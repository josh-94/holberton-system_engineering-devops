#!/usr/bin/python3
'''Script that, using an REST API, for a given employee ID,
returns information about his/her TODO list progress.'''
import requests
import sys


def R_API():
    '''Validate if argument has index and is an interger'''
    try:
        employee_id = int(sys.argv[1])

    except ValueError:
        print('Value Error')
        exit()
    except IndexError:
        print('Index Error')
        exit()
    '''python requets get method'''
    todo = requests.get('https://jsonplaceholder.typicode.com/todos')
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(employee_id))

    name = user.json().get('name')
    total_task = 0
    tasks_done = 0

    tittles = []
    for list_ in todo.json():
        if (list_.get('userId') == employee_id):
            total_task += 1
            if (list_.get('completed') is True):
                tasks_done += 1
                tittles.append(list_.get('title'))

    print("Employee {} is done with tasks({}/{}):"
          .format(name, tasks_done, total_task))
    for tittle in tittles:
        print("\t {}".format(tittle))


if __name__ == "__main__":
    R_API()
