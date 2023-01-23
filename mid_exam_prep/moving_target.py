def shoot(list1, index, power):
    if len(list1) > index >= 0:
        if list1[index] <= power:
            list1.pop(index)
        else:
            list1[index] -= power


def add(list1, index, value):
    if len(list1) > index >= 0:
        list1.insert(index, value)
    else:
        return print("Invalid placement!")


def strike(list1, index, radius):
    if index + radius >= len(list1) or index - radius < 0:
        return print("Strike missed!")
    else:
        for current_index in list1[index - radius: index + radius + 1]:
                list1.remove(current_index)



targets = [int(x) for x in input().split()]

command = input()

while not command == "End":
    command, ind, val = command.split(" ")

    if command == "Shoot":
        shoot(targets, int(ind), int(val))

    elif command == "Add":
        add(targets, int(ind), int(val))

    elif command == "Strike":
        strike(targets, int(ind), int(val))

    command = input()

targets = [str(x) for x in targets]
print("|".join(targets))