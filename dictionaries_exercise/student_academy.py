input_line = int(input())

result = {}

for _ in range(input_line):
    name = input()
    grade = float(input())

    if name not in result:
        result[name] = []
    result[name].append(grade)

for key, value in result.items():
    score = sum(value) / len(value)
    if score >= 4.50:
        print(f"{key} -> {score:.2f}")
