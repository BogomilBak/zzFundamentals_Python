def absolution(list_1):
    for index in range(len(list_1)):
        list_1[index] = abs(list_1[index])
    return list_1


input_line = [float(x) for x in input().split()]
result = absolution(input_line)
print(result)
