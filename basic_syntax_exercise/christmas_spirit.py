quantity = int(input())
days = int(input())

money_spent = 0
points = 0

for current_day in range(1, days + 1):
    flag_1 = False
    if current_day % 11 == 0:
        quantity += 2
    if current_day % 2 == 0:
        money_spent += quantity * 2
        points += 5
    if current_day % 3 == 0:
        money_spent += quantity * 5
        points += 3
        money_spent += quantity * 3
        points += 10
        flag_1 = True
    if current_day % 5 == 0:
        money_spent += quantity * 15
        points += 17
        if flag_1:
            points += 30

    if current_day % 10 == 0:
        points -= 20
        money_spent += 15 + 5 + 3

if days % 10 == 0:
    points -= 30

print(f"Total cost: {money_spent}")
print(f"Total spirit: {points}")
