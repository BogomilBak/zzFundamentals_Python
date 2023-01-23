input_line = [int(x) for x in input().split()]

command = input()

while not command == "end":

    if command == "decrease":
        input_line = [(x - 1) for x in input_line]
        command = input()
        continue

    command = command.split()

    if command[0] == "swap":
        first = int(command[1])
        second = int(command[2])
        input_line[first], input_line[second] = input_line[second], input_line[first]

    elif command[0] == "multiply":
        first = int(command[1])
        second = int(command[2])
        input_line[first] *= input_line[second]

    command = input()

input_line = [str(x) for x in input_line]
print(', '.join(input_line))
