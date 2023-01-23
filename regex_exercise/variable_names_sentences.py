import re

input_line = input()

patter = r"(^_|(?<=\s_))[A-Za-z0-9]+\b"

result = [x.group() for x in re.finditer(patter, input_line)]

print(','.join(result))