initial_energy = int(input())
current_energy = initial_energy
won = 0
counter = 0
flag = True
command = input()

while not command == "End of battle":
    command = int(command)
    counter += 1
    if current_energy >= command:
        current_energy -= command
        won += 1
    else:
        flag = False
        break

    if counter == 3:
        counter = 0
        current_energy += won
    command = input()


if flag:
    print(f"Won battles: {won}. Energy left: {current_energy}")
else:
    print(f"Not enough energy! Game ends with {won} won battles and {current_energy} energy")
