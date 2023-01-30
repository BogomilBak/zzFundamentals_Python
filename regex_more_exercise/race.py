import re

participants = input().split(", ")

input_line = input()

name_pattern = r""
distance_pattern = r"\d"
result = {}

while not input_line == "end of race":
    for name in participants:
        name_pattern = rf"[{name}]"
        match = re.findall(name_pattern, input_line)
        if ''.join(match) == name:
            if name not in result:
                result[name] = 0
            distance = [int(x) for x in re.findall(distance_pattern, input_line)]
            distance = sum(distance)
            result[name] += distance
            break

    input_line = input()

sorted_result = sorted(result.items(), key=lambda x: -x[1])
counter = 1
for key, value in sorted_result:
    if counter == 1:
        print(f"1st place: {key}")
    elif counter == 2:
        print(f"2nd place: {key}")
    elif counter == 3:
        print(f"3rd place: {key}")
    counter += 1
