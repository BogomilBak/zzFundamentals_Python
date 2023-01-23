input_line = int(input())

for number in range(1, input_line + 1):
    digits_sum = 0
    digits = number
    while digits > 0:
        digits_sum += digits % 10
        digits = digits // 10

    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")