input_line = input()

result = {}
total_submissions = {}

while not input_line == "exam finished":

    if "banned" in input_line:
        name, command = input_line.split("-")
        if name in result:
            del result[name]


    else:
        name, language, score = input_line.split("-")
        score = int(score)

        if language not in total_submissions:
            total_submissions[language] = 0
        total_submissions[language] += 1

        if name not in result:
            result[name] = 0

        if score > result[name]:
            result[name] = score

    input_line = input()

print("Results:")

for key, value in result.items():
    print(f"{key} | {value}")

print("Submissions:")

for key, value in total_submissions.items():
    print(f"{key} - {value}")