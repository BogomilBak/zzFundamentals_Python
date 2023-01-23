input_line = input()

result = ""
cut_string = ""
index = 0
while index < len(input_line):
    if input_line[index] == ">" and input_line[index + 1].isalnum():
        strength = int(input_line[index + 1])
        cut_string = input_line[index:index + strength + 1]
        for explosion in range(strength + 1):
            if cut_string[explosion].isalnum():
                to_remove = cut_string[explosion]
                cut_string = cut_string.replace(to_remove, "")
        result += cut_string

    else:
        result += input_line[index]
        index += 1
