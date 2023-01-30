import re

input_line = input()

pattern = r"(?<=(=|/))[A-Z][a-zA-Z]{2}([a-zA-Z]+)?(?=\1)"

match = [x.group() for x in re.finditer(pattern, input_line)]

count = sum([len(x) for x in match])

print(f"Destinations: {', '.join(match)}")
print(f"Travel Points: {count}")
