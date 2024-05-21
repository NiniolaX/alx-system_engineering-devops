#!/usr/bin/python3
"""
Contains a function that returns information about an employees TODO list
progress.
"""
import requests
import sys


def get_employee_name(employee_id):
    """ Returns the name of employee """
    url = 'https://jsonplaceholder.typicode.com/users'
    try:
        response = requests.get(f'{url}/{employee_id}')
        if response.status_code == 200:
            employee = response.json()
            return employee.get('name')
        else:
            print(f'Error fetching user: {response.status_code}')
    except Exception as e:
        print(e)


def get_employee_tasks(employee_id):
    """ Returns all employees tasks """
    url = 'https://jsonplaceholder.typicode.com/todos'
    params = {'userId': employee_id}
    try:
        response.get(url, params)
        if response.status_code == 200:
            tasks = response.json()
            return tasks
        else:
            print(f'Error fetching employee tasks: {response.status_code}')
    except Exception as e:
        print(e)


def get_tasks_done(tasks):
    """ Returns titles of tasks done by an employee """
    tasks_done = []
    for task in tasks:
        if task.get('completed') = True:
            tasks_done.append(task)
    return tasks_done


def display_task_progress(name, number_of_tasks, number_of_completed_tasks,
                          titles):
    """ Prints the task progress of an employee """
    print(f'Employee {name} is done with tasks(\
            {number_of_completed_tasks}/{number_of_tasks}):')
    for title in titles:
        print(f'\t {title}')


def main()
    """
    Displays an employees TODO list progress using
    """
    # Fetch employee
    employee_name = get_employee_name(employee_id)

    # Fetch employee's todos
    tasks = get_employee_tasks(employee_id)
    number_of_tasks = len(tasks)

    # Get number of tasks completed by employee
    tasks_completed = get_tasks_done(tasks)
    number_of_tasks_completed = len(tasks_completed)
    # Get titles of completed tasks
    titles_of_completed_tasks = []
    for task in tasks_completed:
        titles_of_completed_tasks.append(task.get('title'))

    # Output progress
    display_task_progress(employee_name, number_of_tasks,
            number_of_tasks_completed, titles_of_completed_tasks)


if __name__ == '__main__':
    main()
