lines = int(input())

for _ in range(lines):
    input_line = input()

    name_start_index = input_line.index("@")
    name_end_index = input_line.index("|")

    age_start_index = input_line.index("#") - 1
    age_end_index = input_line.index("*")

    name = input_line[name_start_index + 1:name_end_index]
    age = input_line[age_start_index + 2:age_end_index]

    print(f"{name} is {age} years old.")