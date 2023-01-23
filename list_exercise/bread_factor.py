input_line = input().split("|")
energy = 100
coins = 100
flag = True
for i in range(len(input_line)):
    current_activity = input_line[i].split("-")
    if current_activity[0] == "rest":
        energy_gained = int(current_activity[1])

        if energy + energy_gained > 100:
           energy_gained = 100 - energy

        energy += energy_gained

        print(f"You gained {energy_gained} energy.")
        print(f"Current energy: {energy}.")
    elif current_activity[0] == "order":
        if energy >= 30:
            coins += int(current_activity[1])
            energy -= 30
            print(f"You earned {int(current_activity[1])} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= int(current_activity[1]):
            coins -= int(current_activity[1])
            print(f"You bought {current_activity[0]}.")
        else:
            print(f"Closed! Cannot afford {current_activity[0]}.")
            flag = False
            break
if flag:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")