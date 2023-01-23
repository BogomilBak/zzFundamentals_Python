rooms = input().split("|")

initial_health = 100
initial_bitcoins = 0

for room in rooms:
    command, number = room.split()
    number = int(number)

    if command == "potion":
        if initial_health + number >= 100:
            heal_amount = 100 - initial_health
            initial_health = 100
            print(f"You healed for {heal_amount} hp.")

        else:
            initial_health += number
            print(f"You healed for {number} hp.")

        print(f"Current health: {initial_health} hp.")

    elif command == "chest":
        initial_bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        if initial_health - number <= 0:
            print(f"You died! Killed by {command}.")
            best_room = rooms.index(room) + 1
            print(f"Best room: {best_room}")
            initial_health = 0
            break
        else:
            initial_health -= number
            print(f"You slayed {command}.")

if initial_health > 0:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")



