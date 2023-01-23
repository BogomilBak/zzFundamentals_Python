input_line = input().split("|")
budget = float(input())
current_budget = budget
profit = 0
profit_list = []
for index in input_line:
    current_index = index.split("->")
    type_clothing = current_index[0]
    price = float(current_index[1])

    if type_clothing == "Clothes" and price <= 50 and current_budget >= price:
        current_budget -= price
        profit += 0.4 * price
        this_profit = (price * 0.4)
        profit_list.append(price * 1.4)
    elif type_clothing == "Shoes" and price <= 35 and current_budget >= price:
        current_budget -= price
        profit += 0.4 * price
        profit_list.append(price * 1.4)
    elif type_clothing == "Accessories" and price <= 20.5 and current_budget >= price:
        current_budget -= price
        profit += 0.4 * price
        profit_list.append(price * 1.4)

for profit_1 in profit_list:
    print(f"{profit_1:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")

if profit + budget >= 150:
    print(f"Hello, France!")
else:
    print("Not enough money.")