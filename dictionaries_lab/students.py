result = {}

input_line = input()

while ":" in input_line:

    name, student_id, course = input_line.split(":")
    student_id = int(student_id)
    result[name] = [student_id, course]

    input_line = input()

if "_" in input_line:
    input_line = input_line.split("_")

    for key, element in result.items():
        if input_line[0] in element[1]:
            print(f"{key} - {element[0]}")

else:
    for key, element in result.items():
        if input_line in element[1]:
            print(f"{key} - {element[0]}")
