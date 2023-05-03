import csv

with open("laptops.csv", mode="r") as infile:
    thing = list(csv.reader(infile, delimiter = "\n"))
    headers = thing[0][0]
    headers = headers.split(",")

    thingDict = {}

    for i in range(1, len(thing)):
        line = thing[i][0].split(",")
        for i in range(len(line)):
            if headers[i] not in thingDict.keys():
                thingDict[headers[i]] = [line[i]]
            elif headers[i] in thingDict.keys():
                thingDict[headers[i]].append(line[i])

print(thingDict[headers[1]][3])


def getspecs():
    while True:
        ram = input("how much ram would you like, 4GB, 8GB, 16GB or 32GB > ").upper()
        if ram in thingDict[headers[6]]:
            print("men")
            break
        else:
            print("invalid input please try again")
    tempcpu = []
    for i in thingDict[headers[5]]:
        cum = i.upper().split()
        cum = cum[1:3]
        cum = " ".join(cum)
        tempcpu.append(cum)
        thingDict[headers[5]] = tempcpu
    while True:
        cpuinput = input("what kind of cpu would you like, Core i3, Core i5 or Core i7 > ").upper()
        if cpuinput in thingDict[headers[5]]:
            print("dudes")
            break
        else:
            print("invalid input please try again")
    while True:
        ssd = input("how much SSD storage would you like 128GB SSD, 256GB SSD, 512GB SSD, 1TB SSD, 500GB HDD, 1TB HDD or 2TB HDD> ").upper()
        if ssd in thingDict[headers[7]]:
            print("semen")
            break
        else:
            print("invalid input please try again")
    options = []
    for i in range(1, len(thing)):
        line = thing[i][0].split(",")
        for i in range(len(line)):
            if headers[i] not in options:
                options = [line[i]]
            elif headers[i] in options:
                options.append(line[i])


getspecs()
