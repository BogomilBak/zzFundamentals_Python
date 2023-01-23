import re

input_line = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
matches = re.findall(pattern, input_line)
print(' '.join(matches))
