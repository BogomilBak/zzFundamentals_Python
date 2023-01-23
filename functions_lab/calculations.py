def operation(one, two, three):
    if one == "multiply":
        return two * three
    elif one == "divide":
        return two // three
    elif one == "add":
        return two + three
    elif one == "subtract":
        return two - three

input_line = input()
num_1 = int(input())
num_2 = int(input())

print(operation(input_line, num_1, num_2))
