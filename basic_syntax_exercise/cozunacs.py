budget = float(input())
flour_price = float(input())
price_eggs = flour_price * 0.75
price_1_milk = flour_price * 1.25
price_14_milk = price_1_milk / 4
price_per_cozonac = price_eggs + flour_price + price_14_milk
money_left = budget

counter = 0
colored_eggs = 0

while True:
    if money_left < price_per_cozonac:
        break
    money_left -= price_per_cozonac
    colored_eggs += 3
    counter += 1
    if counter % 3 == 0:
        colored_eggs -= counter - 2

print(f"You made {counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
