initial_list = input().split("!")

command = input()

while not command == "Go Shopping!":
    command = command.split()

    if command[0] == "Urgent":
        item = command[1]
        if item not in initial_list:
            initial_list.insert(0, item)

    elif command[0] == "Unnecessary":
        item = command[1]
        if item in initial_list:
            initial_list.remove(item)

    elif command[0] == "Correct":
        old_item = command[1]
        new_item = command[2]
        if old_item in initial_list:
            index = initial_list.index(old_item)
            initial_list.pop(index)
            initial_list.insert(index, new_item)

    elif command[0] == "Rearrange":
        item = command[1]
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)

    command = input()

print(', '.join(initial_list))