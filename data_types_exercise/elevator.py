persons = int(input())
capacity = int(input())

counter = 0
persons_remaining = persons
while True:
    persons_remaining -= capacity
    counter += 1
    if persons_remaining <= 0:
        break

print(counter)