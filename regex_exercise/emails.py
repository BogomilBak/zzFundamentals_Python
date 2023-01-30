import re

input_line = input()

pattern = r"(^|(?<=\s))[A-Za-z0-9]+[\._-]?[A-Za-z0-9]+@[a-z]+-?[a-z]+(\.[a-z]+)+"

result = [x.group() for x in re.finditer(pattern, input_line)]

print(*result, sep='\n')