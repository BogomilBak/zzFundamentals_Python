input_line = input()

last_index = 0
result = ""
unique_symbols = []

for index in range(len(input_line)):
    if input_line[index].isdigit() and not input_line[index - 1].isdigit():
        if not index == len(input_line) - 1:
            if not input_line[index + 1].isdigit():
                current_digit = int(input_line[index])
                if last_index == 0:
                    current_letters = input_line[:index].upper()
                    last_index = index + 1
                else:
                    current_letters = input_line[last_index:index].upper()
                    last_index = index + 1

            else:
                current_digit = f"{input_line[index]}{input_line[index + 1]}"
                current_digit = int(current_digit)

                if last_index == 0:
                    current_letters = input_line[:index].upper()
                    last_index = index + 2
                else:
                    current_letters = input_line[last_index:index].upper()
                    last_index = index + 2

        else:
            current_digit = int(input_line[index])
            if last_index == 0:
                current_letters = input_line[:index].upper()
                last_index = index + 1
            else:
                current_letters = input_line[last_index:index].upper()
                last_index = index + 1

        for symbol in current_letters:
            if symbol not in unique_symbols:
                unique_symbols.append(symbol)


        result += current_letters * current_digit

print(f"Unique symbols used: {len(unique_symbols)}")
print(result)


