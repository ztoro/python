# OLVASÁS
f = open("./input/score.csv", "r")
for x in f:
    print(x.rstrip())  # rstrip kiszedi a /n-t!
    currentline = x.split(",")
    print(currentline[0])
    print(currentline[1].rstrip())
f.close()

