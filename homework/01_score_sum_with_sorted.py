# A meglévő függvények és adatszerkezetek segítségével, funkcionális programozási paradigmával a score.csv file-ból
# egy python script segítségével mutasd meg, hogy kinek összesen hány pontja lett, és ki lett az első, második, és
# harmadik helyezett! A megoldás legyen a játékosok számától független!


def main():
    file = open("../input/score.csv", "r")
    result_list = []
    for line in file:
        name, score = get_processing_inputs(line)
        add_result(name, score, result_list)
    file.close()
    # használjuk a beépített sorted függvényt, aminek az egyik paramétere, a key, lehet akár egy függvény is!
    ranked_result = sorted(result_list, key=get_score, reverse=True)
    write_winners(ranked_result)


def get_processing_inputs(line):
    current_line = line.split(",")
    name = current_line[0]
    score = int(current_line[1].rstrip())
    return name, score

def add_result(name, score, result_list):
    found = False
    for result in result_list:
        if result["name"] == name:
            current_score = result["total_score"] + score
            print(f"Adding {score} to {result["total_score"]} for player {result["name"]}: "
                  f"Current score is {current_score}")  # print fstring példa
            result["total_score"] = current_score
            found = True
            break
    if not found:
        print(f"Creating new player with name {name} and score {score}")
        result_list.append({"name": name, "total_score": score})


def get_score(player):
    return player["total_score"]


def write_winners(ranked_result):
    try:  # ("Easier to Ask For Forgiveness Than Permission", vagyis EAFP - ez így "Pythonic")
        print(f"1st place: {ranked_result[0]["name"]} with {ranked_result[0]["total_score"]}")
        print(f"2nd place: {ranked_result[1]["name"]} with {ranked_result[1]["total_score"]}")
        print(f"3rd place: {ranked_result[2]["name"]} with {ranked_result[2]["total_score"]}")
    except IndexError:
        pass


main()
