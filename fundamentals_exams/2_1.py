def add_stop(a, b, c):
    if len(a) > b:
        left_part = a[:b]
        right_part = a[b:]
        a = left_part + c + right_part
        print(a)
        return a
    print(a)
    return a

def remove_stop(a, b, c):
    if len(a) > b and len(a) > c:
        left_part = a[:b]
        right_part = a[c + 1:]
        a = left_part + right_part
        print(a)
        return a
    print(a)
    return a

def switch(a, b, c):
    if b in a:
        a = a.replace(b, c)
        print(a)
        return a
    print(a)
    return a


word = input()
input_line = input()

while not input_line == "Travel":
    input_line = input_line.split(":")
    command = input_line[0]

    if command == "Add Stop":
       word = add_stop(word, int(input_line[1]), input_line[2])

    elif command == "Remove Stop":
        word =remove_stop(word, int(input_line[1]), int(input_line[2]))

    elif command == "Switch":
        word = switch(word, input_line[1], input_line[2])

    input_line = input()

print(f"Ready for world tour! Planned stops: {word}")
