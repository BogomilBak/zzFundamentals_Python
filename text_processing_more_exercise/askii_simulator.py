first_ch = input()
second_ch = input()
input_line = input()

result = 0

first_ch = ord(first_ch)
second_ch = ord(second_ch)

for element in input_line:
    if first_ch < ord(element) < second_ch:
        result += ord(element)

print(result)