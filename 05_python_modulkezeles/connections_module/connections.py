import requests


def get_data():
    r = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    print(r.status_code)
    print(r.json())


def write_hello_world():
    print("hello world!")
