import re

input_line = input()
pattern = r">>(?P<name>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)"

furniture_all = []
spent_money = 0

while not input_line == "Purchase":
    match = re.match(pattern, input_line)
    if match:
        match = match.groupdict()
        furniture = match['name']
        furniture_all.append(furniture)
        spent_money += int(match['quantity']) * float(match['price'])
    input_line = input()

print('Bought furniture:')
if furniture_all:
    print('\n'.join(furniture_all))
print(f"Total money spend: {spent_money:.2f}")
