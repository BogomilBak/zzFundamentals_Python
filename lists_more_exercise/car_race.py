input_line = input().split()

middle = len(input_line) // 2
left_side = input_line[0:middle]
right_side = input_line[(middle + 1):]

left_result = 0
right_result = 0

for left_lap in left_side:
    number = int(left_lap)
    if number == 0:
        left_result = left_result * 0.8
        continue
    left_result += number

for right_lap in reversed(right_side):
    number = int(right_lap)
    if number == 0:
        right_result = right_result * 0.8
        continue
    right_result += number

if left_result < right_result:
    print(f"The winner is left with total time: {left_result:.1f}")
else:
    print(f"The winner is right with total time: {right_result:.1f}")
