input_line = input().split()
number = int(input())
result = []
counter = 0
while not len(input_line) == len(result):
    for current_number in input_line:
        if not current_number in result:
            counter += 1
            if counter == number:
                result.append(current_number)
                counter = 0
result = [int(x) for x in result]
print(str(result).replace(' ', ''))
