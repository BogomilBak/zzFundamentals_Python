import re

input_line = input()

pattern = r"(#|\|)(?P<name>[A-Za-z]+(\s)?([A-Za-z]+)?)\1(?P<expiration>\d{2}\/\d{2}/\d{2})\1(?P<calories>\d+)\1"
calories = 0
match = [x.groupdict() for x in re.finditer(pattern, input_line)]

for element in match:
    for key in element:
        if key == "calories":
            calories += int(element[key])

days_left = calories // 2000

print(f"You have food to last you for: {days_left} days!")

for element in match:
    print(f"Item: {element['name']}, Best before: {element['expiration']}, Nutrition: {element['calories']}")
