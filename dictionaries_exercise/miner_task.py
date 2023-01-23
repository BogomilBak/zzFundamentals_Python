input_line = input()
result = {}
counter = 1
material = ""
while not input_line == "stop":
    if counter == 1:
        if input_line not in result:
            result[input_line] = 0
        material = input_line
        counter = 2
    else:
        result[material] += int(input_line)
        counter = 1
    input_line = input()

for key, value in result.items():
    print(f"{key} -> {value}")