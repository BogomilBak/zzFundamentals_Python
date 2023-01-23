input_line = input()
digits = ""
letters = ""
other = ""

for element in input_line:
    if element.isdigit():
        digits += element

    elif element.isalpha():
        letters += element

    else:
        other += element

print(digits)
print(letters)
print(other)