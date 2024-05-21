#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format.
"""
import json
import requests


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com"
    user_url = f"{url}/users"
    todos_url = f"{url}/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)
    user_data = user_response.json()
    todos_data = todos_response.json()

    with open("todo_all_employees.json", "w") as file:

        data = {}
        for todo in todos_data:
            row = {}
            user_id = todo.get("userId")
            row['task'] = todo.get("title")
            row['completed'] = todo.get("completed")
            row['username'] = user_data[user_id - 1]["username"]

            if user_id not in data:
                data[user_id] = []

            data[user_id].append(row)

        json.dump(data, file)
