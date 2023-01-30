lines = int(input())

result = {}

for _ in range(lines):
    hero, health, mana = input().split()
    health = int(health)
    mana = int(mana)

    if health > 100:
        health = 100
    if mana > 200:
        mana = 200

    result[hero] = {'health': health, 'mana': mana}

input_line = input()

while not input_line == "End":
    input_line = input_line.split(" - ")
    command = input_line[0]
    hero = input_line[1]

    if command == "CastSpell":
        mana_needed = int(input_line[2])
        spell_name = input_line[3]

        if mana_needed <= result[hero]['mana']:
            result[hero]['mana'] -= mana_needed
            print(f"{hero} has successfully cast {spell_name} and now has {result[hero]['mana']} MP!")

        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif command == "TakeDamage":
        damage = int(input_line[2])
        attacker = input_line[3]
        result[hero]['health'] -= damage

        if result[hero]['health'] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {result[hero]['health']} HP left!")

        else:
            print(f"{hero} has been killed by {attacker}!")
            del result[hero]

    elif command == "Recharge":
        amount = int(input_line[2])

        if result[hero]['mana'] + amount > 200:
            recovered = 200 - result[hero]['mana']

        else:
            recovered = amount
        result[hero]['mana'] += recovered
        print(f"{hero} recharged for {recovered} MP!")

    elif command == "Heal":
        amount = int(input_line[2])

        if result[hero]['health'] + amount > 100:
            recovered = 100 - result[hero]['health']

        else:
            recovered = amount
        result[hero]['health'] += recovered
        print(f"{hero} healed for {recovered} HP!")

    input_line = input()

for key, value in result.items():
    print(key)
    print(f"  HP: {value['health']}")
    print(f"  MP: {value['mana']}")
