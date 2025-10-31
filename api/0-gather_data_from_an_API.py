#!/usr/bin/env python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 0-gather_data_from_an_API.py <employee_id>")

    emp_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{base_url}/users/{emp_id}").json()
    todos = requests.get(f"{base_url}/todos", params={"userId": emp_id}).json()

    done_tasks = [task for task in todos if task["completed"]]
    print(f"Employee {user['name']} is done with tasks({len(done_tasks)}/{len(todos)}):")
    for task in done_tasks:
        print(f"\t {task['title']}")

