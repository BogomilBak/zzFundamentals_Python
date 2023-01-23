input_line = input().split()
result = {}

for index in range(0, len(input_line), 2):
    result[input_line[index]] = int(input_line[index + 1])

print(result)