f = open("school1.csv",  "r")
for line in f:
    print(repr(line))
f.close()