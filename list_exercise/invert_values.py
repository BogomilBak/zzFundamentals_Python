input_line = input().split()
list_1 = []

for number in input_line:
    number_inverted = int(number) * - 1
    list_1.append(number_inverted)

print(list_1)