input_line = input()

passwords = {}
results = {}

while not input_line == "end of contests":
    contest, password = input_line.split(":")
    passwords[contest] = password

    input_line = input()

input_line = input()

while not input_line == "end of submissions":
    contest, password, name, score = input_line.split("=>")
    score = int(score)

    if contest in passwords:
        if passwords[contest] == password:

            if name not in results:
                results[name] = {}

            if contest not in results[name]:
                results[name][contest] = 0

            if score > results[name][contest]:
                results[name][contest] = score

    input_line = input()

total_scores = {}

for key in results.items():

    if key[0] not in total_scores:
        total_scores[key[0]] = 0

    for values in key[1].values():
        total_scores[key[0]] += values

sorted_total_scores = dict(sorted(total_scores.items(), key=lambda x: -x[1]))

print(f"Best candidate is {list(sorted_total_scores.keys())[0]} with total {list(sorted_total_scores.values())[0]} points.")

print("Ranking:")


sorted_results_alphabet = dict(sorted(results.items(), key=lambda x: x[0]))


for key, value in sorted_results_alphabet.items():
    print(key)

    sorted_value = dict(sorted(value.items(), key=lambda x: -x[1]))

    for key_1, value_1 in sorted_value.items():
        print(f"#  {key_1} -> {value_1}")
