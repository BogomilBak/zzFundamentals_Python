import re

input_line = input()

pattern = r"w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+"

while input_line:
    match = [x.group() for x in re.finditer(pattern, input_line)]
    if match:
        print(match[0])
    input_line = input()
