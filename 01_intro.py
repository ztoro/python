# Python standard library: https://docs.python.org/3/library

# Változó deklarálás, értékadás
var = "hello world"

# Függvény hívás, a print függvény (beépített)
print("hello")
print(var)

# https://docs.python.org/3/library/datetime.html
# Datetime modul és használata:
import datetime  # importálni mindig a file tetején szoktunk, csak prezentációs célzattal van itt!

# import this # the python zen
print(datetime.datetime.now())

# Értékek vizsgálata, összehasonlítása
if 5 == 5:
    print("equal")

############

if 5 != 6:
    print("not equal")

if 5 != 5:
    print("this is not possible!!")
else:
    print("equal")

############

if 5 < 6:
    print("5 is less than 6!")
else:
    print("this is not possible!")

############

if 5 <= 5:
    print("5 is less or equal than 5!")
else:
    print("this is not possible!")

# Ciklus
# Ciklusokat több elemű struktúrákon szoktunk mindig végrehajtani - például listán
# ( array != list, python-ban nincs array! )
list = ["Tibi", "Gabor", "Zoli"]

print("FOR ciklus")
for name in list:
    print(name)


print("WHILE ciklus")
n = len(list)
i = 0
while i < n:
    print(list[i])
    i = i + 1

# Vigyázat! Végtelen ciklus!
infinity = False
while infinity:
    print("INFINITY!!!")

# Ciklusmegszakítás:
print("BREAK")
for name in list:
    if name == "Tibi":
        print(name)
        print("Megtaláltam Tibit!")
        break


# Függvény
# Függvény deklarálás:
def my_function(param1, param2):
    print("my_function fgv hívás!")
    result = param1 + param2
    return result


res = my_function(5, 6)
print(res)
