first_str = input()
second_str = input()
last_string = first_str

for symbol in range(len(first_str)):
    left_part = second_str[:symbol + 1]
    right_part = first_str[symbol + 1:]
    current_string = left_part + right_part
    if current_string == last_string:
        continue
    print(current_string)
    last_string = current_string