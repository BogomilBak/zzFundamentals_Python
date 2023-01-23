import re

input_line = input()
pattern = r"(?P<date>\d{2})(?P<separator>[\.\-\\/])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"

match = [x.groupdict() for x in re.finditer(pattern, input_line)]

print('\n'.join([f"Day: {data['date']}, Month: {data['month']}, Year: {data['year']}" for data in match]))
