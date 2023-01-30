import re

lines = int(input())

pattern_barcode = r"@#+[A-Z][a-zA-Z0-9]{4}([a-zA-Z0-9]+)?[A-Z]@#+"
pattern_group = r"\d+"

for _ in range(lines):
    input_line = input()

    match = [x.group() for x in re.finditer(pattern_barcode, input_line)]

    if match:
        product_group = [x.group() for x in re.finditer(pattern_group, match[0])]
        if product_group:
            if len(product_group) > 1:
                print(f"Product group: {''.join(product_group)}")

            else:
                print(f"Product group: {product_group[0]}")
        else:
            print(f"Product group: 00")

    else:
        print("Invalid barcode")