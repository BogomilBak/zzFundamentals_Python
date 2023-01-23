input_line = input()

result = {}

while not input_line == "buy":
    name, price, quantity = input_line.split()
    price = float(price)
    quantity = int(quantity)

    if name not in result:
        result[name] = {'price': price, 'quantity': quantity}

    else:
        result[name]['price'] = price
        result[name]['quantity'] += quantity

    input_line = input()

for key, value in result.items():
    end_result = result[key]['price'] * result[key]['quantity']
    print(f"{key} -> {end_result:.2f}")
