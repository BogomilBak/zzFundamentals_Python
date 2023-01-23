input_line = input().split("\\")
last_index = len(input_line) - 1
temp_list = input_line[last_index].split(".")

file_name = temp_list[0]
file_extension = temp_list[1]

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")