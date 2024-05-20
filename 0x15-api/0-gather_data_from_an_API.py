#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
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

    done_titles = []
    done_number = 0
    for todo in todos_data:
        if todo.get("completed"):
            done_number += 1
            done_titles.append(todo.get("title"))

    employe_name = user_data.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(employe_name, done_number, len(todos_data)))
    for title in done_titles:
        print("\t {}".format(title))
