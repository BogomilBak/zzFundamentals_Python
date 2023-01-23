import re

input_line = input()
word = input()

pattern = f"\\b{word}\\b"

result = re.findall(pattern, input_line, re.IGNORECASE)
print(len(result))