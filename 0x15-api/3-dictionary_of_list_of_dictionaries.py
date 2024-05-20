#!/usr/bin/python3
""" export data in the JSON format """

import json
import requests
import sys


if __name__ == "__main__":
    jsonplaceholder = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(jsonplaceholder)
    employees = response.json()
    print(employees)

    data_dict = {}

    for employee in employees:
        USER_ID = employee.get('id')
        username = employee.get('username')
        url = '{}/{}/todos'.format(jsonplaceholder, USER_ID)
        response = requests.get(url)
        tasks = response.json()
        data_dict[USER_ID] = []
        for task in tasks:
            data_dict[USER_ID].append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed"),
            })

    with open('todo_all_employees.json', 'w') as f:
        json.dump(data_dict, f)
