#!/usr/bin/python3
"""
Python script that, using JSONPlaceholder REST API, for a given employee ID,
returns information about his/her TODO list progress.
export data in the CSV format
"""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    user_info = requests.get(base_url+"users/"+user_id).json()
    all_todos = requests.get(base_url+"todos",
                             params={"userId": user_id}).json()
    csv_name = f"{user_id}.csv"
    with open(csv_name, 'w') as cs:
        csv_writer = csv.writer(cs, quoting=csv.QUOTE_ALL)
        for todo in all_todos:
            slctd = [todo.get(key, "N/A") for key in ['completed', 'title']]
            line = [user_info.get("id"), user_info.get("username")] + slctd
            csv_writer.writerow(line)
