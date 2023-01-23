input_line = [int(x) for x in input().split()]
command = input()

while not command == "End":
    command = int(command)
    if command < len(input_line):
        if not input_line[command] == -1:
            for index in range(len(input_line)):
                if not input_line[index] == -1 and not index == command:
                    value = input_line[command]
                    if input_line[index] > value:
                        input_line[index] -= value
                    else:
                        input_line[index] += value
        input_line[command] = -1

    command = input()
count = input_line.count(-1)
input_line = [str(x) for x in input_line]
print(f"Shot targets: {count} -> {' '.join(input_line)}")
