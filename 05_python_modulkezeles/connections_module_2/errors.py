# Osztályokról, örököltetésről, még tanulunk a későbbiek folyamán, csak azért van ez a példa
# hogy teljes legyen hogy ezeket hogyan kell használni modul szinten.
# Addig előjáróban:
# Itt létrehozunk egy MyOwnError osztályt, amit a python Exception osztályából származtatunk:
class MyOwnError(Exception):
    # Pythonban az __init__ a konstruktor függvény, az osztály létrehozásakor meghívódik
    def __init__(self):
        super().__init__()
        # A super() függvény meghívja az Exception osztály konstruktorát!
        print("Woohoo! I threw an error!")
