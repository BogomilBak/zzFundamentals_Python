import re

input_line = input()
pattern = r"\+359( |-)2\1\d{3}\1\d{4}\b"
vaid_nums = [obj.group() for obj in re.finditer(pattern, input_line)]
print(', '.join(vaid_nums))