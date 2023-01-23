input_line = input()

result = {}

while not input_line == "no more time":
    username, contest, points = input_line.split(" -> ")
    points = int(points)

    if contest not in result:
        result[contest] = {}

    if username not in result[contest]:
        result[contest][username] = 0

    if points > result[contest][username]:
        result[contest][username] = points

    input_line = input()

for key in result.items():
    print(f"{key[0]}: {len(list(key[1]))} participants")
    counter = 1
    sorted_scores = dict(sorted(key[1].items(), key=lambda x: (-x[1], x[0])))

    for key_1, element in sorted_scores.items():
        print(f"{counter}. {key_1} <::> {element}")
        counter += 1

print(f"Individual standings:")

individual_result = {}

for key in result.values():
    for key_1, value in key.items():
        if key_1 not in individual_result:
            individual_result[key_1] = 0
        individual_result[key_1] += value

individual_result = dict(sorted(individual_result.items(), key=lambda x: (-x[1], x[0])))
counter = 1
for key, value in individual_result.items():

    print(f"{counter}. {key} -> {value}")
    counter += 1



