#!/usr/bin/python3

import requests
import sys


def fetch_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    employee_url = f"{base_url}/users/{employee_id}"
    response = requests.get(employee_url)
    if response.status_code != 200:
        print(f"Error: Unable to fetch employee details for ID {employee_id}")
        return
    employee_data = response.json()
    employee_name = employee_data.get("name")

    todos_url = f"{base_url}/todos?userId={employee_id}"
    response = requests.get(todos_url)
    if response.status_code != 200:
        print(f"Error: Unable to fetch TODO list for ID {employee_id}")
        return
    todos_data = response.json()

    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} \
    is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    fetch_employee_todo_progress(employee_id)
