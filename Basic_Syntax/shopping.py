budget = int(input())

remaining_budget = budget
flag = False

while True:
    input_line = input()
    if input_line == "End":
        break
    input_line = int(input_line)
    if input_line > remaining_budget:
        flag = True
        break
    remaining_budget -= input_line

if flag:
    print(f"You went in overdraft!")
else:
    print(f"You bought everything needed.")
