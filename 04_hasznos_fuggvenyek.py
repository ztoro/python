# OLVASÁS
f = open("./input/score.csv", "r")
for x in f:
  print(x)
  currentline = x.split(",")
  print(currentline[0])
  print(currentline[1])
f.close()

