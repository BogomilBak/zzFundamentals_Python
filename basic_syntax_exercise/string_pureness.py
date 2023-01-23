number = int(input())

for i in range(number):
    input_line = input()
    flag = False
    for a in input_line:
        if a == "," or a == "." or a == "_":
            flag = True
            break
    if flag:
        print(f"{input_line} is not pure!")
    else:
        print(f"{input_line} is pure.")