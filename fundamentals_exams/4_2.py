import re

input_line = input()

pattern = r"(@|#)[A-Za-z][A-Za-z][A-Za-z]+\1\1[A-Za-z][A-Za-z][A-Za-z]+\1"

match = [x.group() for x in re.finditer(pattern, input_line)]
result = []
for element in match:
    middle = int(len(element) / 2)
    left_part = element[:middle]
    right_part = element[middle:]
    reversed_right = right_part[::-1]
    if left_part == reversed_right:
        result_left_item = left_part[1:-1]
        result_right_item = right_part[1:-1]
        result_item = f"{result_left_item} <=> {result_right_item}"
        result.append(result_item)
if match:
    print(f"{len(match)} word pairs found!")
else:
    print(f"No word pairs found!")
if result:
    print('The mirror words are:')
    print(f"{', '.join(result)}")
else:
    print("No mirror words!")
