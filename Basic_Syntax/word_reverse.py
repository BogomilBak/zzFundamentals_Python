input_line = input()

reversed_word = ""

for letter in range(len(input_line) - 1, -1, -1):
    reversed_word += input_line[letter]
print(reversed_word)
