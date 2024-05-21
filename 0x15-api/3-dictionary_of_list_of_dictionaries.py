#!/usr/bin/python3
"""
Python script that, using JSONPlaceholder REST API, for all employees,
returns information about his/her TODO list progress.
export data in JSON format
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    base_url = "https://jsonplaceholder.typicode.com/"
    users_info = requests.get(base_url+"users/").json()
    all_tasks = {}
    for each in users_info:
        user_id = each.get("id")
        username = each.get("username")
        todos = requests.get(base_url+"todos",
                             params={"userId": user_id}).json()

        # pythonic dict in a list
        list_tasks = [{"username": username,
                       "task": todo.get('title'),
                       "completed": todo.get("completed")
                       }
                      for todo in todos]
        all_tasks[user_id] = list_tasks
        jf = "todo_all_employees.json"
        # dumping python to json
    with open(jf, 'w') as jsonfile:
        json.dump(all_tasks, jsonfile)
