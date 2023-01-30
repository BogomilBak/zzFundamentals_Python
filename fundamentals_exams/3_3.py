input_line = input()

result = {}

while not input_line == "Sail":
    town, population, gold = input_line.split("||")
    population = int(population)
    gold = int(gold)
    if town not in result:
        result[town] = {'population': population, 'gold': gold}
    else:
        result[town]['population'] += population
        result[town]['gold'] += gold
    input_line = input()

input_line = input()

while not input_line == "End":
    input_line = input_line.split("=>")
    command = input_line[0]

    if command == "Plunder":
        town = input_line[1]
        people = int(input_line[2])
        gold = int(input_line[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        result[town]['population'] -= people
        result[town]['gold'] -= gold
        if result[town]['population'] <= 0 or result[town]['gold'] <= 0:
            print(f"{town} has been wiped off the map!")
            del result[town]
    elif command == "Prosper":
        town = input_line[1]
        gold = int(input_line[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            result[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {result[town]['gold']} gold.")

    input_line = input()

if result:
    print(f"Ahoy, Captain! There are {len(result)} wealthy settlements to go to:")
    for key, value in result.items():
        print(f"{key} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
