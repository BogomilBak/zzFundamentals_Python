number_of_lines = int(input())
counter = 0
for i in range(number_of_lines):
    letter = input()
    counter += ord(letter)

print(f"The sum equals: {counter}")
