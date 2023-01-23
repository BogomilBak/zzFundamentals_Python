input_line = input()

result = {}

while not input_line == "Once upon a time":
    name, color, physics = input_line.split(" <:> ")
    physics = int(physics)

    if color not in result:
        result[color] = {}

    if name not in result[color]:
        result[color][name] = 0

    if physics > result[color][name]:
        result[color][name] = physics


    input_line = input()

sorted_result = {}

for key, value in result.items():
    if key not in sorted_result:
        sorted_result[key] = []

    for key_1, value_1 in value.items():
        if key_1 not in sorted_result[key]:
            sorted_result[key].append(key_1)
            sorted_result[key].append(value_1)

sorted_result = sorted(sorted_result.items(), key=lambda x: -x[1])
print(sorted_result)





