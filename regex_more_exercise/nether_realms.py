import re

input_line = input()
base_pattern = r"[^\s,]+"
input_line = re.findall(base_pattern, input_line)

name_pattern = r"[^0-9+*/.-]"
positive_pattern = r"(?<!\-|\.)\d+(\.\d+)?"
negative_pattern = r"(?<=\-)\d+(\.\d+)?"
result = {}
for name in input_line:

    health_list = re.findall(name_pattern, name)
    health_value = sum([ord(x) for x in health_list])

    positive_list = [float(x.group()) for x in re.finditer(positive_pattern, name)]
    negative_list = [float(x.group()) for x in re.finditer(negative_pattern, name)]

    damage_raw = sum(positive_list) - sum(negative_list)

    for symbol in name:
        if symbol == "*":
            damage_raw *= 2
        elif symbol == "/":
            damage_raw /= 2

    if name not in result:
        result[name] = {'health': health_value, 'damage': damage_raw}

sorted_result = sorted(result.items(), key=lambda x: x[0])

for key, value in sorted_result:
    print(f"{key} - {value['health']} health, {value['damage']:.2f} damage")

