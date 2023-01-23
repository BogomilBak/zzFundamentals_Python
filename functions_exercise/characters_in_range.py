def askii_function(a, b):
    for character in range(ord(a) + 1, ord(b)):
        print(chr(character), end=" ")


input_1 = input()
input_2 = input()

askii_function(input_1, input_2)
