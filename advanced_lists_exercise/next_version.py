input_line = input().split(".")
# if input_line[1] == "9" and input_line[2] == "9":
#     input_line[0] = str(int(input_line[0]) + 1)
#     input_line[1] = "0"
#     input_line[2] = "0"
# elif input_line[2] == "9":
#     input_line[1] = str(int(input_line[1]) + 1)
#     input_line[-1] = "0"
# else:
#     input_line[2] = str(int(input_line[2]) + 1)
input_line = "".join(input_line)
input_line = int(input_line)
input_line += 1
input_line = str(input_line)
input_line = [str(f" {x}" for x in input_line)]
print(input_line)
