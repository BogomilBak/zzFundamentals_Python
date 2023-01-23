def data_type(first, second):
    if first == "string":
        return f"${second}$"
    elif first == "real":
        temp_var = float(second) * 1.5
        return f"{temp_var:.2f}"
    elif first == "int":
        return 2 * int(second)


input_line_1 = input()
input_line_2 = input()
print(data_type(input_line_1, input_line_2))
