number = int(input())

flag = False

for i in range(1, number + 1):
    number_2 = int(input())
    if number_2 % 2 != 0:
        flag = True
        break

if flag:
    print(f"{number_2} is odd!")
else:
    print("All numbers are even.")