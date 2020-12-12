
f = open("day5.txt", "r")

f1 = f.readlines()

ids = [0]
counter = 979

for l in f1:
    min = 0
    max = 127
    indicator = 128
    minRow = 0
    maxRow = 7
    indicatorRow = 8
    # print(l)
    for c in l:
        indicator = indicator / 2
        if c == "F":
            max = max - indicator
            # print("F - Min:", min , "Max:", max )
        elif c == "B":
            min = min + indicator
            # print("B - Min:", min , "Max:", max )
        elif c == "L":
            indicatorRow = indicatorRow / 2
            maxRow = maxRow - indicatorRow
            # print("L - MinRow:", minRow , "MaxRow:", maxRow )
        elif c == "R":
            indicatorRow = indicatorRow / 2
            minRow = minRow + indicatorRow
            # print("R - MinRow:", minRow , "MaxRow:", maxRow )
    ID = (max * 8) + maxRow
    ids.append(ID)

ids.sort(reverse=True)
print(ids[0])

for id in ids:
    upper = ids.count(counter + 1)
    pos = ids.count(counter)
    lower = ids.count(counter - 1)
    if upper == 1 and pos == 0 and lower == 1:
        print(counter , "isnt on the list but", (counter + 1) ,"and", (counter - 1) ,"are")
    counter = counter - 1
        
        


            