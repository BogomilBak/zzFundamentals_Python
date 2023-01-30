activation_key = input()

input_line = input()

while not input_line == "Generate":
    input_line = input_line.split(">>>")
    command = input_line[0]

    if command == "Contains":
        if input_line[1] in activation_key:
            print(f"{activation_key} contains {input_line[1]}")
        else:
            print("Substring not found!")

    elif command == "Flip":
        operation = input_line[1]
        start_index = int(input_line[2])
        end_index = int(input_line[3])
        left_part = activation_key[:start_index]
        right_part = activation_key[end_index:]
        middle_part = activation_key[start_index:end_index]
        if operation == "Upper":
            middle_part = middle_part.upper()

        else:
            middle_part = middle_part.lower()

        activation_key = left_part + middle_part + right_part
        print(activation_key)

    elif command == "Slice":
        start_index = int(input_line[1])
        end_index = int(input_line[2])
        left_part = activation_key[:start_index]
        right_part = activation_key[end_index:]
        activation_key = left_part + right_part
        print(activation_key)

    input_line = input()

print(f"Your activation key is: {activation_key}")