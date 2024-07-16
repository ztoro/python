# A feladat: az alábbi REST API-n menjünk végig az összes poston és kommenten, és keressük meg a
# legrövidebb és a leghosszabb bejegyzéseket! Ezeket a bejegyzéseket írjuk ki egy tetszőlegesen elnvezett file-ba az
# ../output mappa (vagy más, egyénileg választott mappa) alá!
# 'https://jsonplaceholder.typicode.com/'
import requests


def main():
    urls = ['https://jsonplaceholder.typicode.com/posts/', 'https://jsonplaceholder.typicode.com/comments/']
    min_string, max_string = get_max_and_min_comments(urls)
    write_to_file(min_string, max_string)


def get_max_and_min_comments(urls):
    max_length = 0
    max_string = ""
    min_length = 0
    min_string = "kiskutakiskuta"
    initialized = False

    for url in urls:
        r = requests.get(url)
        for item in r.json():
            body = item["body"].rstrip()
            if not initialized:
                min_length = len(r.json()[0]["body"])
                print(r.json()[0])
                initialized = True
                print(f"Initialized! {min_length}")
            string_length = len(body)
            if max_length < string_length:
                max_length = string_length
                max_string = item["body"]
            if min_length > string_length and body:
                min_length = string_length
                min_string = item["body"]

    return min_string, max_string


def write_to_file(min_string, max_string):
    file = open("../output/output.txt", "w")
    file.write(f"{max_string}\n")
    file.write("\n")
    file.write(f"{min_string}\n")
    file.close()


if __name__ == '__main__':
    print(__name__)
    main()
