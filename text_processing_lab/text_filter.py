banned = input().split(", ")
input_line = input()

for ban in range(len(banned)):
    word = banned[ban]
    while word in input_line:
        amount = len(banned[ban])
        input_line = input_line.replace(banned[ban], "*" * amount)

print(input_line)