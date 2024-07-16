import connections_module_2
#  És végül, importálhatjuk magát a modult is, csak akkor fel kell készíteni erre az init.py-t!


def main():
    print("Hello")
    print("__name__ value: ", __name__)
    print("python main function")
    print(connections_module_2.PACKAGE_VERSION)
    connections_module_2.get_data()
    connections_module_2.write_hello_world()
    try:
        raise connections_module_2.MyOwnError
    except connections_module_2.MyOwnError:
        print("I caught my error!")


if __name__ == '__main__':
    main()
# Csak akkor hajtódik végre a main, ha a main.py van futtatva direkt!
