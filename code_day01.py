# Advent Of Code 2022 Day 1

snackinventory = 'input_day01.txt'

### Stupid solution with ranking ###

snacklist = list()                          # Create an empty list to fill with depth numbers
snackgroup = list()
grouprecord = 0
snackrecord = 0
rank1 = 0
rank2 = 0
rank3 = 0
snackrecord3 = 0

with open(snackinventory) as f:             # Read the input file
    lines = f.readlines()                   # Read each line as a string
    for line in lines:
        if len(line) > 1:                   # For each line:
            snackgroup.append(int(line))    # Convert the string to an int and stor it in the list
        elif len(line) == 1:
            snacklist.append(snackgroup)
            for snack in snackgroup:
                grouprecord += snack
                if grouprecord > rank1:
                    rank3 = rank2
                    rank2 = rank1
                    rank1 = grouprecord
                elif grouprecord > rank2:
                    rank3 = rank2
                    rank2 = grouprecord
                elif grouprecord > rank3:
                    rank3 = grouprecord
            grouprecord = 0
            snackgroup = list()

snackrecord3 = rank1 + rank2 + rank3
print(rank1)                                # Solution part 1
print(snackrecord3)                         # Solution part 2


### Smarter solution with list sorting ###

snacksum = 0
snacksums = list()
elfsnackgroup = list()

with open(snackinventory) as f:             # Read the input file
    lines = f.readlines()                   # Read each line as a string
    for line in lines:
        if len(line) > 1:                   # For each line:
            elfsnackgroup.append(int(line))    # Convert the string to an int and stor it in the list
            snacksum += int(line)
        elif len(line) == 1:
            snacklist.append(elfsnackgroup)
            snacksums.append(snacksum)
            snacksum = 0

snacksums.sort()
snacksums.reverse()
print(snacksums[0])
print(sum(snacksums[0:3]))

