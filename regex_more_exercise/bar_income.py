import re

input_line = input()
total_money = 0
pattern = r"%(?P<name>[A-Z][a-z]+)%[^|$%.]*?<(?P<product>[A-Za-z0-9]+)>[^|$%.]*?\|(?P<quantity>\d+)\|[^|$%.]*?(?P<price>\d+(\.\d+)?)\$"

while not input_line == "end of shift":
    match = re.match(pattern, input_line)
    if match:
        match = match.groupdict()
        product_price = int(match['quantity']) * float(match['price'])
        print(f"{match['name']}: {match['product']} - {product_price:.2f}")
        total_money += product_price
    input_line = input()

print(f"Total income: {total_money:.2f}")
