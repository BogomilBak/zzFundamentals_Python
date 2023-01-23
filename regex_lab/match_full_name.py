import re

input_line = input().split(", ")

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

result = []

for name in input_line:
    match = re.match(pattern, name)
    if match:
        result.append(match.group())

print(' '.join(result))
