input_line = input()
result = {}

while not input_line == "statistics":
    input_line = input_line.split(": ")

    if input_line[0] in result:
        result[input_line[0]] += int(input_line[1])

    else:
        result[input_line[0]] = int(input_line[1])

    input_line = input()

print(f"Products in stock:")
for key, value in result.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(result)}")
print(f"Total Quantity: {sum(result.values())}")
