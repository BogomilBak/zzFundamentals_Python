input_line = input()
result = {}

for element in input_line:
    if element == " ":
        continue

    if element not in result:
        result[element] = 0
    result[element] += 1

for key, value in result.items():
    print(f"{key} -> {value}")
