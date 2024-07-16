from connections_module.connections import get_data
# Vagy importálhatunk csak egy függvényt is


def main():
    print("Hello")
    print("__name__ value: ", __name__)
    print("python main function")
    get_data()
    # write_hello_world()  # ez hibát dobna, nincs ilyen függvényünk!


if __name__ == '__main__':
    main()
# Csak akkor hajtódik végre a main, ha a main.py van futtatva direkt!
