import requests


def get_data():
    r = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    print(r.status_code)
    print(r.json())


def write_hello_world():
    print("Hello world!")


def main():
    print("Show me the money!")


# Vigyázat! Itt is van egy main() függvényünk, viszont emiatt a feltétel miatt nem fut le az importálás folyamán!
print(f"Hello! My module name is {__name__}")
if __name__ == '__main__':
    main()
