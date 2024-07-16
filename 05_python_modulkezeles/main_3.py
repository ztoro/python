from connections_module.connections import get_data as my_original_function
#  Ez a get_data függvény, csak átneveztük! Így lehet lekezelni a névütközést például


def main():
    print("Hello")
    print("__name__ value: ", __name__)
    print("python main function")
    my_original_function()  # Ez a get_data függvény, csak átneveztük!


if __name__ == '__main__':
    main()
# Csak akkor hajtódik végre a main, ha a main.py van futtatva direkt!
