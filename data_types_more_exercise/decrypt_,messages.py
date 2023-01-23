key = int(input())
total_lines = int(input())
result = []
for num in range(total_lines):
    input_line = input()
    current_digit = ord(input_line) + key
    result.append(chr(current_digit))

print("".join(result))
