#!/usr/bin/python3
'''A script that, uses a REST API, for a given employee ID,returns
information about his/her TODO list progress.
Usage:
   ./0-gather_data_from_an_API.py <id>
Author:
    Abdulsalam Abdulsomad .A. - April 24th, 2023.
'''
import requests
import sys


API = "https://jsonplaceholder.typicode.com"
if __name__ == "__main__":
    if len(sys.argv) > 1:
        ID = int(sys.argv[1])
        if ID > 0:
            # Get all todos
            todos_req = requests.get("{}/todos".format(API)).json()
            # gets the user with the id provided
            user_req = requests.get("{}/users/{}".format(API, ID)).json()
            # retrieve name of user
            user_name = user_req.get('name')
            # get a list of all todos of the user
            user_todos = []
            for todo in todos_req:
                if todo.get('userId') == ID:
                    user_todos.append(todo)
            # get a list of completed todos
            completed_todo = []
            for todo in user_todos:
                if todo.get('completed'):
                    completed_todo.append(todo)
            print("Employee {} is done with tasks({}/{}):"
                  .format(
                      user_name,
                      len(completed_todo),
                      len(user_todos)
                      )
                  )
            for task in completed_todo:
                print("\t {}".format(task.get('title')))
