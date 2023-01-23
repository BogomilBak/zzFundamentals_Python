import re

input_line = input()
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

result = [x.group() for x in re.finditer(pattern, input_line)]

print(' '.join(result))