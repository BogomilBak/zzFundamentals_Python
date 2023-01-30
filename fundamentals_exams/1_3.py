def add(a, b, c, d):
    if b in a:
        print(f"{b} is already in the collection!")
        return a
    a[b] = [c, d]
    print(f"{b} by {c} in {d} added to the collection!")
    return a


def remove(a, b):
    if b not in a:
        print(f"Invalid operation! {b} does not exist in the collection.")
        return a
    a.pop(b)
    print(f"Successfully removed {b}!")
    return a


def change(a, b, c):
    if b not in a:
        print(f"Invalid operation! {b} does not exist in the collection.")
        return a
    a[b][1] = c
    print(f"Changed the key of {b} to {c}!")
    return a


lines = int(input())

result = {}

for _ in range(lines):
    piece, author, key = input_line = input().split("|")
    result[piece] = [author, key]

input_line = input()

while not input_line == "Stop":
    input_line = input_line.split("|")
    command = input_line[0]

    if command == "Add":
        add(result, input_line[1], input_line[2], input_line[3])

    elif command == "Remove":
        remove(result, input_line[1])

    elif command == "ChangeKey":
        change(result, input_line[1], input_line[2])

    input_line = input()

for piece, value in result.items():
    print(f"{piece} -> Composer: {value[0]}, Key: {value[1]}")
