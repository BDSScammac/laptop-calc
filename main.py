import csv

# opening and splitting the csv file into variables
with open("laptops.csv", mode="r") as infile:
    rows = list(csv.reader(infile, delimiter = "\n"))
    headers = rows[0][0]
    headers = headers.split(",")

    # empty dict to add to from csv file
    laptopDict = {}

    # adding all items from csv file into dict
    for i in range(1, len(rows)):
        line = rows[i][0].split(",")
        for i in range(len(line)):
            if headers[i] not in laptopDict.keys():
                laptopDict[headers[i]] = [line[i]]
            elif headers[i] in laptopDict.keys():
                laptopDict[headers[i]].append(line[i])


# function for finding price range based off user input
def pricing(ram, cpuinput, storage):
    # empty list to add prices to
    options = []
    # adding every price that fits inputs into list
    for i in range(len(laptopDict[headers[0]])):
        if laptopDict[headers[6]][i] == ram and laptopDict[headers[5]][i] == cpuinput and laptopDict[headers[7]][i] == storage:
            options.append(float(laptopDict[headers[12]][i]))
    # sorting the inputs from lowest to highest
    options.sort()
    # returning the list so it can be used later
    return options


def getspecs():
    # getting user ram
    while True:
        ram = input("how much ram would you like, 4GB, 8GB, 16GB or 32GB > ").upper()
        if ram in laptopDict[headers[6]]:
            print(f"you have selected {ram}")
            break
        else:
            print("invalid input please try again")
    # sorting cpu so that only the 2nd and 3rd words are taken from dict
    tempcpu = []
    for i in laptopDict[headers[5]]:
        cpu = i.lower().split()
        cpu = cpu[1:3]
        cpu = " ".join(cpu)
        tempcpu.append(cpu)
        laptopDict[headers[5]] = tempcpu
    # getting user cpu
    while True:
        cpuinput = input("what kind of cpu would you like, Core i3, Core i5 or Core i7 > ").lower()
        if cpuinput in laptopDict[headers[5]]:
            print(f"your have selected {cpuinput}")
            break
        else:
            print("invalid input please try again")
    # getting user storage
    while True:
        storage = input("how much SSD storage would you like 128GB SSD, 256GB SSD, 512GB SSD, 1TB SSD, 500GB HDD, 1TB HDD or 2TB HDD> ").upper()
        if storage in laptopDict[headers[7]]:
            print(f"you have selected {storage}")
            break
        else:
            print("invalid input please try again")
    # returning variables
    return [ram, cpuinput, storage]


# calling getspecs function
specs = getspecs()
# calling pricing function and adding inputs from getspecs
options = pricing(specs[0], specs[1], specs[2])
# checking there is a laptop that fits
if len(options) > 0:
    # printing price range
    print(f"your laptop will cost {options[0]} - {options[-1]} Euros")
else:
    print("no laptops fit these specifications")
