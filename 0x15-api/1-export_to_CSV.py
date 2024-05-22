#!/usr/bin/python3
"""
Contains a function that returns all an employee's tasks and progress
and exports them in CSV format.
"""
import csv
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
    """ Returns all tasks of an employee
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


def write_data_to_csv(csv_file_path, tasks, employee_id, employee_username):
    """ Writes JSON data to CSV file
    Args:
        csv_file_path(str): Path to CSV file
        tasks(list of dicts): Data to write into CSV file
        employee_id(int): Employee's id
        employee_username(str): Employee's username
    Return:
        None
    """
    # Write tasks to CSV file
    with open(csv_file_path, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        # Write the data
        for task in tasks:
            completion_status = "True" if task.get('completed') else "False"
            task_title = task.get('title')
            writer.writerow([employee_id, employee_username,
                            completion_status, task_title])


def main():
    """
    Fetches an employee's task information and exports it to a CSV file
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

    # Write data to CSV file
    path_to_csv = f'{employee_id}.csv'
    write_data_to_csv(path_to_csv, tasks, employee_id, employee_username)


if __name__ == '__main__':
    main()
