#!/usr/bin/python3

import requests
import sys


if __name__ == "__main__":
    uid = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    name = user.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    alltasks = 0
    done = 0

    for task in todos.json():
        if task.get('uid') == int(uid):
            alltasks += 1
            if tasks.get('completed'):
                done += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(userId) and task.get('completed')]))
