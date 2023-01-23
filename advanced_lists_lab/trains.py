input_line = int(input())
example_list = [0] * input_line
command = input()

while "End" not in command:
    command = command.split()
    if command[0] == "add":
        example_list[-1] += int(command[1])
    elif command[0] == "insert":
        index = int(command[1])
        example_list[index] += int(command[2])
    elif command[0] == "leave":
        index = int(command[1])
        example_list[index] -= int(command[2])

    command = input()

print(example_list)
