
f = open("day5.txt", "r")

f1 = f.readlines()

min = 1
max = 128
ids = []

for l in f1:
    for c in l:
        if c == "F":
            