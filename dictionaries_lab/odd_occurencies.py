input_line = input().split()

result = {}

for element in input_line:
    current_element = element.lower()
    if current_element not in result:
        result[current_element] = 0
    result[current_element] += 1

for key, values in result.items():
    if not values % 2 == 0:
        print(key, end=' ')