input_line = [int(x) for x in input().split("@")]

command = input()
position = 0
max_position = len(input_line)

while not command == "Love!":
    command = command.split()
    jump = int(command[1])
    position += jump

    if position >= max_position:
        position = 0

    if input_line[position] == 0:
        print(f"Place {position} already had Valentine's day.")
        command = input()
        continue

    input_line[position] -= 2

    if input_line[position] == 0:
        print(f"Place {position} has Valentine's day.")


    command = input()

win = input_line.count(0)
fail = max_position - win
print(f"Cupid's last position was {position}.")

if fail > 0:
    print(f"Cupid has failed {fail} places.")
else:
    print(f"Mission was successful.")
