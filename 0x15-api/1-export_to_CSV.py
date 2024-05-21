#!/usr/bin/python3
"""exports data in the CSV format"""

import requests
from sys import argv


if __name__ == "__main":
    uid = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(uid))
    name = user.json().get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')


    file = f"{id}.csv"
    with open(file, "w") as f:
        for item in todos:
            f.write(f'"{id}","{user["username"]}","{item["completed"]}", \
                "{item["title"]}"\n')
