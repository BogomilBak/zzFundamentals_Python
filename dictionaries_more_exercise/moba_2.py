input_line = input()

result = {}
total_skill = {}
while not input_line == "Season end":

    if "->" in input_line:
        name, position, skill = input_line.split(" -> ")
        skill = int(skill)

        if name not in result:
            result[name] = {}

        if position not in result[name]:
            result[name][position] = skill

        if skill > result[name][position]:
            result[name][position] = skill

        if name not in total_skill:
            total_skill[name] = 0
        total_skill[name] += skill

    else:
        first, second = input_line.split(" vs ")

        if first in result and second in result:

            for key in result[first].keys():
                if key in result[second].keys():

                    first_value = result[first][key]
                    second_value = result[second][key]

                    if first_value > second_value:
                        del total_skill[second]
                        del result[second]
                        break

                    elif first_value < second_value:
                        del total_skill[first]
                        del result[second]
                        break

                    else:
                        break

    input_line = input()

sorted_result = {}

for key, value in result.items():
    if key not in sorted_result:
        sorted_result[key] = 0

        for score in value.values():
            sorted_result[key] += score

sorted_result = dict(sorted(sorted_result.items(), key=lambda x: (-x[1], x[0])))

for key, value in sorted_result.items():
    print(f"{key}: {value} skill")

    for key_1, value_1 in sorted(result[key].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {key_1} <::> {value_1}")
