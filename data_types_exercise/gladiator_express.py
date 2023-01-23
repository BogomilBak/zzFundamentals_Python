losses_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_sum = 0
counter = 0

for current_loss in range(1, losses_count + 1):
    if current_loss % 2 == 0:
        total_sum += helmet_price
    if current_loss % 3 == 0:
        total_sum += sword_price
        if current_loss % 2 == 0:
            total_sum += shield_price
            counter += 1
            if counter == 2:
                total_sum += armor_price
                counter = 0

print(f"Gladiator expenses: {total_sum:.2f} aureus")

