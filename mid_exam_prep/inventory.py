journal = input().split(", ")

initial_command = input()

while not initial_command == "Craft!":
    initial_command = initial_command.split(" - ")
    command = initial_command[0]
    resource = initial_command[1]
    if command == "Collect":
        if resource not in journal:
            journal.append(resource)
    elif command == "Drop":
        if resource in journal:
            journal.remove(resource)
    elif command == "Combine Items":
        resource = resource.split(":")
        old_item = resource[0]
        new_item = resource[1]
        if old_item in journal:
            old_item_index = journal.index(old_item) + 1
            journal.insert(old_item_index, new_item)
    elif command == "Renew":
        if resource in journal:
            journal.remove(resource)
            journal.append(resource)

    initial_command = input()

print(', '.join(journal))
