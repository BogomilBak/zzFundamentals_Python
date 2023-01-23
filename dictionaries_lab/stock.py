input_line = input().split()
check_items = input().split()
products = {}

for element in range(0, len(input_line), 2):
    products[input_line[element]] = int(input_line[element + 1])

for element in check_items:
    if element in input_line:
        print(f"We have {products[element]} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")
