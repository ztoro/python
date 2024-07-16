from connections_module import connections
# Importálhatjuk a python file-t a modulon belül


def main():
    print("Hello")
    print("__name__ value: ", __name__)
    print("python main function")
    connections.get_data()
    connections.write_hello_world()


if __name__ == '__main__':
    main()
# Csak akkor hajtódik végre a main, ha a main.py van futtatva direkt!
