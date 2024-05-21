#!/usr/bin/python3
"""
Python script that, using JSONPlaceholder REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import requests
    import sys

    user_id = sys.argv[1]
    # root address of the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com/"
    # .json() parses the response as JSON and
    # returns a Python dictionary
    user_info = requests.get(base_url+"users/"+user_id).json()
    all_todos = requests.get(base_url+"todos",
                             params={"userId": user_id}).json()
    compl_todos = requests.get(base_url+"todos",
                               params={"userId": user_id,
                                       "completed": "true"}).json()
    # total num of tasks
    n_tasks = len(all_todos)
    # done tasks
    n_compl = len(compl_todos)

    print(f"Employee {user_info.get('name')} is done with tasks"
          f"({n_compl}/{n_tasks}):")
    for task in compl_todos:
        print("\t", task["title"])
