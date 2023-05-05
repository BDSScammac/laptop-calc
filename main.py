import csv


def file():
    # opening and splitting the csv file into variables
    with open("laptops.csv", mode="r") as infile:
        rows = list(csv.reader(infile, delimiter = "\n"))
        headers = rows[0][0]
        headers = headers.split(",")

        # empty dict to add to from csv file
        laptopdict = {}

        # adding all items from csv file into dict
        for i in range(1, len(rows)):
            line = rows[i][0].split(",")
            for i in range(len(line)):
                if headers[i] not in laptopdict.keys():
                    laptopdict[headers[i]] = [line[i]]
                elif headers[i] in laptopdict.keys():
                    laptopdict[headers[i]].append(line[i])
    return [laptopdict, headers]


# function for finding price range based off user input
def pricing(ram, cpuinput, storage, laptopdict, headers):
    # empty list to add prices to
    options = []
    # adding every price that fits inputs into list
    for i in range(len(laptopdict[headers[0]])):
        if laptopdict[headers[6]][i] == ram and laptopdict[headers[5]][i] == cpuinput and laptopdict[headers[7]][i] == storage:
            options.append(float(laptopdict[headers[12]][i]))
    # sorting the inputs from lowest to highest
    options.sort()
    # returning the list so it can be used later
    return options


# gets inputs from user
def get_specs():
    # constants
    ram_options = ["4GB", "8GB", "16GB", "32GB"]
    cpu_options = ["core i3", "core i5", "core i7"]
    storage_options = ["128GB SSD", "256GB SSD", "512GB SSD", "1TB SSD", "500GB HDD", "1TB HDD", "2TB HDD"]
    # getting user ram
    while True:
        ram = input(f"how much ram would you like {ram_options} > ").upper()
        if ram in ram_options:
            print(f"you have selected {ram}")
            break
        else:
            print("invalid input please try again")
    # sorting cpu so that only the 2nd and 3rd words are taken from dict
    tempcpu = []
    for i in laptopdict[headers[5]]:
        cpu = i.lower().split()
        cpu = cpu[1:3]
        cpu = " ".join(cpu)
        tempcpu.append(cpu)
        laptopdict[headers[5]] = tempcpu
    # getting user cpu
    while True:
        cpuinput = input(f"what kind of cpu would you like, {cpu_options} > ").lower()
        if cpuinput in cpu_options:
            print(f"your have selected {cpuinput}")
            break
        else:
            print("invalid input please try again")
    # getting user storage
    while True:
        storage = input(f"how much SSD storage would you like {storage_options} > ").upper()
        if storage in storage_options:
            print(f"you have selected {storage}")
            break
        else:
            print("invalid input please try again")
    # returning variables
    return [ram, cpuinput, storage]


laptopdict, headers = file()
# calling getspecs function
specs = get_specs()
# calling pricing function and adding inputs from getspecs
options = pricing(specs[0], specs[1], specs[2], laptopdict, headers)
# checking there is a laptop that fits
if len(options) > 0:
    # printing price range
    print(f"your laptop will cost {options[0]} - {options[-1]} Euros")
else:
    print("no laptops fit these specifications")
