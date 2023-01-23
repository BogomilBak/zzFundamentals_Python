input_line = input()

result = {}

while not input_line == "buy":
    product, price, quantity = input_line.split()
    price = float(price)
    quantity = int(quantity)

    if product not in result:
        result[product] = [price, quantity]

    else:
        new_quantity = result[product][1] + quantity
        result[product] = [price, new_quantity]

    input_line = input()

for key, value in result.items():
    final_value = value[0] * value[1]
    print(f"{key} -> {final_value:.2f}")


