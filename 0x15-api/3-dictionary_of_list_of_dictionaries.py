#!/usr/bin/python3
"""
Contains a function that returns all an employee's tasks and progress
and exports them in CSV format.
"""
import json
import requests


def get_all_tasks():
    """ Returns all tasks
    Args:
        None
    Return:
        (list of dicts): List of all tasks or 1 on error
    """
    url = 'https://jsonplaceholder.typicode.com/todos'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            tasks = response.json()
            return tasks
        else:
            print(f"Error fetching employee's tasks: {response.status_code}")
            return 1
    except Exception as e:
        print(e)


def get_all_employees():
    """ Returns all employees
    Args:
        None
    Return:
        (list of dicts): List of all employees or 1 on error
    """
    url = 'https://jsonplaceholder.typicode.com/users'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            employees = response.json()
            return employees
        else:
            print(f"Error fetching employees: {response.status_code}")
            return 1
    except Exception as e:
        print(e)
        return 1


def sort_tasks(tasks, users):
    """ Sort tasks by user
    Args:
        tasks(list of dicts): All tasks
        users(list of dicts): All users
    Return:
        (dicts of lists of dicts): Sorted data
    """
    sorted_tasks = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        user_tasks = []
        for task in tasks:
            if task.get('userId') == user_id:
                title = task.get('title')
                status = task.get('completed')
                user_tasks.append({'username': username, 'task': title,
                                  'completed': status})
        sorted_tasks[user_id] = user_tasks

    return sorted_tasks


def main():
    """
    Fetches an all tasks sorted by employee and exports them to a JSON file.
    """
    # Get all employees
    employees = get_all_employees()
    if employees == 1:
        return 1

    # Get all tasks
    tasks = get_all_tasks()
    if tasks == 1:
        return 1

    # Sort tasks by employee
    sorted_tasks = sort_tasks(tasks, employees)

    # Write sorted tasks to JSON file
    path_to_json = 'todo_all_employees.json'
    with open(path_to_json, mode='w') as json_file:
        json.dump(sorted_tasks, json_file)


if __name__ == '__main__':
    main()
