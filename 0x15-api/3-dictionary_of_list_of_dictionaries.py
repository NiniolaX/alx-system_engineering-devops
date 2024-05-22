#!/usr/bin/python3
"""
Contains a function that returns all an employee's tasks and progress
and exports them in CSV format.
"""
import json
import requests
import sys


def get_employee_username(employee_id):
    """ Returns the username of an employee
    Args:
        employee_id(int): Empolyee's id
    Return:
        (str): Username of employee
    """
    url = 'https://jsonplaceholder.typicode.com/users'
    try:
        response = requests.get(f'{url}/{employee_id}')
        if response.status_code == 200:
            employee = response.json()
            return employee.get('username')
        else:
            print(f'Error fetching employee: {response.status_code}')
    except Exception as e:
        print(e)


def get_employee_tasks(employee_id):
    """ Returns all employees tasks
    Args:
        employee_id(int): ID of employee
    Return:
        (list of dicts): List of all employee's tasks
    """
    url = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': employee_id}
    try:
        response = requests.get(url, params)
        if response.status_code == 200:
            tasks = response.json()
            return tasks
        else:
            print(f"Error fetching employee's tasks: {response.status_code}")
    except Exception as e:
        print(e)


def display_task_progress(name, number_of_tasks, number_of_completed_tasks,
                          titles):
    """ Prints the task progress of an employee """
    print(f'Employee {name} is done with tasks', end="")
    print(f'({number_of_completed_tasks}/{number_of_tasks}):')
    for title in titles:
        print(f'\t {title}')


def write_data_to_json(json_file_path, tasks, employee_id, employee_username):
    """ Writes JSON data to CSV file
    Args:
        json_file_path(str): Path to JSON file
        tasks(list of dicts): Data to write into CSV file
        employee_id(int): Employee's id
        employee_username(str): Employee's username
    Return:
        None
    """
    # Put data in specified format
    data = {}
    key = employee_id
    val = []
    for task in tasks:
        title = task.get('title')
        status = task.get('completed')
        username = employee_username
        val.append({'task': title, 'completed': status, 'username': username})
    data[key] = val

    # Dump data in JSON file
    with open(json_file_path, mode='w') as json_file:
        json.dump(data, json_file)


def main():
    """
    Fetches an employee's task progress and exports them to a JSON file.
    """
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <employee_id>')
        return 1

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print('Invalid employee id')
        return 1

    # Get employee's name
    employee_username = get_employee_username(employee_id)

    # Fetch employee's tasks
    tasks = get_employee_tasks(employee_id)
    number_of_tasks = len(tasks)

    # Write data to JSON file
    path_to_json = f'{employee_id}.json'
    write_data_to_json(path_to_json, tasks, employee_id, employee_username)


if __name__ == '__main__':
    main()
