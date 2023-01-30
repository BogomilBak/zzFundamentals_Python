word = input()

input_line = input()

while not input_line == "Reveal":
    input_line = input_line.split(":|:")

    if input_line[0] == "InsertSpace":
        index = int(input_line[1])
        word = word[:index] + " " + word[index:]

    elif input_line[0] == "Reverse":
        substring = input_line[1]

        if substring in word:
            reversed_substring = substring[::-1]
            word = word.replace(substring, '', 1)
            word += reversed_substring

        else:
            print("error")
            input_line = input()
            continue

    elif input_line[0] == "ChangeAll":
        substring = input_line[1]
        replacement = input_line[2]
        word = word.replace(substring, replacement)

    print(word)
    input_line = input()

print(f"You have a new text message: {word}")
