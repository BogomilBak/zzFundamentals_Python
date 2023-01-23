import re

input_line = input()

pattern = r"\d+"

final_result = []

while not input_line == "":
    result = re.findall(pattern, input_line)
    final_result.extend(result)
    input_line = input()

print(' '.join(final_result))

