#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format.
"""
import csv
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

    with open('{}.csv'.format(emp_id), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for t in todos_data:
            writer.writerow([emp_id, user_data.get("username"),
                            t.get("completed"), t.get("title")])
