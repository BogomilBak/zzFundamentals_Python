input_line = input().split()
number = int(input())
result = []
counter = 0
index = 0
while len(input_line) > 0:
    counter += 1
    if counter == number:
        result.append(input_line.pop(index))
        counter = 0
    else:
        index += 1
    if index >= len(input_line):
        index = 0

print(str(result).replace(' ', '').replace('\'', ''))