# OLVASÁS
print("======FILEREAD==========")
file = open("./input/score.csv", "r")
for line in file:
    print(line.rstrip())  # rstrip kiszedi a /n-t!
    currentline = line.split(",")
    print(currentline[0])
    print(currentline[1].rstrip())
    my_num = int(currentline[1].rstrip())
    print(my_num)
file.close()


# REQUEST LIBRARY
# https://requests.readthedocs.io/en/latest/
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
import requests
print("======GET REQUESTS==========")
# GET
r = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(r.status_code)  # Kiiratjuk a HTTP status code-ot
print(r.json())  # Kiiratjuk a REST API választ json formátumban (de ez a json lehet lista, dictionary!)
# https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON
print(r.json()["userId"])  # Példa, hogy ez speciel tényleg dictionary, annak összes pro és kontrájával

r = requests.get('https://jsonplaceholder.typicode.com/posts')
print(r.status_code)  # Kiiratjuk a HTTP status code-ot
print(r.json())  # A GET requestre ez a végpont egy dictekből álló listával válaszol! (python szempontból)

# POST
print("======POST REQUESTS==========")
payload = {
    "userId": 1,
    "title": "my first post!",
    "body": "hello world!"
}
r = requests.post('https://jsonplaceholder.typicode.com/posts', data=payload)
print(r.status_code)  # 201-es HTTP status code!
print(r.json())

# PUT, DELETE, stb. HTTP hívások az előzőekhez hasonlóan lehetségesek, lásd a fenti linken a dokumentációt


