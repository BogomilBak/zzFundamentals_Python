number_lines = int(input())
counter = 0
counter_1 = 0
flag = True
for i in range(number_lines):
    input_line = input()
    if input_line == "(":
        counter += 1
    elif input_line == ")":
        counter -= 1
    if counter > 1 or counter < 0:
        flag = False
        break

if flag:
    print("BALANCED")
else:
    print("UNBALANCED")

