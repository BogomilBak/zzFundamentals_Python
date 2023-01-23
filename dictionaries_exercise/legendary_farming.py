input_line = input()

legendary = {'shards': "Shadowmourne", 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
legendary_items = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}

flag = False

while not flag:
    input_line = input_line.split()

    for element in range(0, len(input_line), 2):
        quantity = int(input_line[element])
        item = input_line[element + 1].lower()

        if item in legendary_items:
            legendary_items[item] += quantity

        else:
            if item not in junk:
                junk[item] = 0
            junk[item] += quantity

        for item, quantity in legendary_items.items():
            if quantity >= 250:
                legendary_items[item] -= 250
                print(f"{legendary[item]} has been obtained!")
                flag = True
                break

        if flag:
            break
    if flag:
        break

    input_line = input()

sorted_legendary_items = sorted(legendary_items.items(), key=lambda kvp: (-kvp[1], kvp[0]))

sorted_junk = sorted(junk.items(), key=lambda kvp: kvp[0])

for key, value in sorted_legendary_items:
    print(f"{key}: {value}")

for key, value in sorted_junk:
    print(f"{key}: {value}")
