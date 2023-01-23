keys = [int(x) for x in input().split()]

input_line = input()

while not input_line == "find":
    treasure = ""
    for key in keys:

        for element in range(len(input_line)):
            old_element = input_line[element]
            new_element = chr(ord(input_line[element]) - key)
            treasure += new_element

        input_line = treasure
        treasure = ""

    input_line = input()