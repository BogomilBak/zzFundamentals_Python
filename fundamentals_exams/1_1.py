def move(x, y):

    for a in range(y):
        current_number = x[0]
        del x[0]
        x.append(current_number)
    return x


def insert(x, y, z):
    x.insert(y, z)
    return x


def change_all(x, y, z):
    for index in range(len(x)):
        if x[index] == y:
            x[index] = z

    return x


word = list(input())

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