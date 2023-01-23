input_line = input()

result = {}

while not input_line == "end":
    course, name = input_line.split(" : ")
    if course not in result:
        result[course] = []
    result[course].append(name)

    input_line = input()

for key, value in result.items():
    print(f"{key}: {len(value)}")
    for index in range(len(value)):
        print(f"-- {value[index]}")