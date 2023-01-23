def bill(product, quantity):
    if product == "water":
        return 1 * quantity
    elif product == "coffee":
        return 1.5 * quantity
    elif product == "coke":
        return 1.4 * quantity
    elif product == "snacks":
        return 2 * quantity


ordered_product = input()
quantity_ordered = float(input())
end_result = bill(ordered_product, quantity_ordered)
print(f"{end_result:.2f}")
