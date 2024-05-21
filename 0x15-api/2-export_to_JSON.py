#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":

    emp_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user_url = f"{url}/users/{emp_id}"
    todos_url = f"{url}/todos?userId={emp_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)
    user_data = user_response.json()
    todos_data = todos_response.json()

    with open("{}.json".format(emp_id), "w") as file:
        row_list = []
        data = {}
        for todo in todos_data:
            row = {}
            row['task'] = todo.get("title")
            row['completed'] = todo.get("completed")
            row['username'] = user_data.get("username")
            row_list.append(row)

        data[emp_id] = row_list
        json.dump(data, file)
