gifts_wanted = input().split()
while True:
    input_line = input()
    if input_line == "No Money":
        break
    input_line = input_line.split()
    command = input_line[0]
    current_gift = input_line[1]
    if command == "OutOfStock":
        for index in range(len(gifts_wanted)):
            if gifts_wanted[index] == current_gift:
                gifts_wanted[index] = "None"
    elif command == "Required":
        current_number = int(input_line[2])
        if current_number < len(gifts_wanted):
            gifts_wanted[current_number] = current_gift

    elif command == "JustInCase":
        gifts_wanted[-1] = current_gift

while "None" in gifts_wanted:
    gifts_wanted.remove("None")

print(" ".join(gifts_wanted))


