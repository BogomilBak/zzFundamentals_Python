number_of_orders = int(input())
total_price = 0
for days in range(number_of_orders):
    total_sum = 0
    price_capsule = float(input())
    days_total = int(input())
    capsules_per_day = int(input())
    if 0.01 <= price_capsule <= 100 and 1 <= days_total <= 31 and 1 <= capsules_per_day <= 2000:
        total_sum = capsules_per_day * price_capsule * days_total
        total_price += total_sum
        print(f"The price for the coffee is: ${total_sum:.2f}")
print(f"Total: ${total_price:.2f}")
