input_line = input().split()

result = ""

for element in input_line:
    result += element * len(element)

print(result)