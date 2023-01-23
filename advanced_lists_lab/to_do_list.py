example_list = [0] * 10
input_line = input()

while not input_line == "End":
    index, assignment = input_line.split("-")
    index = int(index) - 1
    example_list.insert(index, assignment)

    input_line = input()

example_list = [x for x in example_list if not x == 0]
print(example_list)