input_line = [int(x) for x in input().split(", ")]
counter = 1
templist = []
while len(input_line) > 0:
    for el in input_line:
        if el <= counter * 10:
            templist.append(el)
    print(f"Group of {counter}0's: {templist}")
    for el in templist:
        input_line.remove(el)
    templist.clear()
    counter += 1
