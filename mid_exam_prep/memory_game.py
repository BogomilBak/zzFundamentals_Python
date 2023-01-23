input_line = input().split()

command = input()
moves_so_far = 0
flag = True

while not command == "end" and input_line:
    first, second = command.split()
    first = int(first)
    second = int(second)
    first_value = input_line[first]
    second_value = input_line[second]
    moves_so_far += 1

    if first == second or first < 0 or first >= len(input_line) or second < 0 or second >= len(input_line):
        middle = len(input_line) // 2
        input_line.insert(middle, f"-{str(moves_so_far)}a")
        input_line.insert(middle, f"-{str(moves_so_far)}a")
        print("Invalid input! Adding additional elements to the board")

    elif first_value == second_value:
        print(f"Congrats! You have found matching elements - {first_value}!")
        input_line.remove(first_value)
        input_line.remove(second_value)

    elif not first_value == second_value:
        print("Try again!")

    command = input()

if not input_line:
    print(f"You have won in {moves_so_far} turns!")
    flag = False

if flag:
    print("Sorry you lose :(")
    if input_line:
        print(f"{' '.join(input_line)}")
