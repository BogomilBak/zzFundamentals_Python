input_line_1 = input().split(", ")
input_line_2 = input().split(", ")
result = []

for element in input_line_1:
    for el in input_line_2:
        if element in el:
            result.append(element)

print(sorted(set(result), key=result.index))
