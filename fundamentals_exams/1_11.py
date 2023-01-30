def move(x, y):
    first_part = x[:y]
    second_part = x[y:]
    x = second_part + first_part
    return x


def insert(x, y, z):
    first_part = x[:y]
    second_part = x[y:]
    x = first_part + z + second_part
    return x


def change_all(x, y, z):
    x = x.replace(y, z)
    return x


word = input()

input_line = input()

while not input_line == "Decode":
    input_line = input_line.split("|")
    command = input_line[0]

    if command == "Move":
        word = move(word, int(input_line[1]))

    elif command == "Insert":
        word = insert(word, int(input_line[1]), input_line[2])

    elif command == "ChangeAll":
        word = change_all(word, input_line[1], input_line[2])

    input_line = input()

print(f"The decrypted message is: {''.join(word)}")