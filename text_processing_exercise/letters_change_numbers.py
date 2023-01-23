input_line = [x.strip() for x in input().split()]

result = 0

for string in input_line:
    first_letter = string[0]
    second_letter = string[-1]
    digits = string[1:(len(string)) - 1]
    digits = int(digits)
    first_letter_position = ord(first_letter.lower()) - 96
    second_letter_position = ord(second_letter.lower()) - 96
    if first_letter.isupper():
        result += digits / first_letter_position
    elif first_letter.islower():
        result += digits * first_letter_position

    if second_letter.isupper():
        result -= second_letter_position
    elif second_letter.islower():
        result += second_letter_position

print(f"{result:.2f}")