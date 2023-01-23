input_line = input().split(", ")
result = {}

for element in input_line:
    el = ord(element)
    result[element] = el

print(result)