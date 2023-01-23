number = int(input())

for a in range(1, number + 1):
    for b in range(1, a + 1):
        print("*", end="")
    print()
for c in range(number - 1, - 1, -1):
    for d in range(c - 1, - 1, -1):
        print("*", end="")
    print()