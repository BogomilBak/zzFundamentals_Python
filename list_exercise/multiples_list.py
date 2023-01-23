factor = int(input())
counter = int(input())
list_1 = []
for number in range(factor, factor * counter + 1, factor):
    list_1.append(number)

print(list_1)