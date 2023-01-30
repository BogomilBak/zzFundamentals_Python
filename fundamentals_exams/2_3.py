lines = int(input())

result = {}

for _ in range(lines):
    plant, rarity = input().split("<->")
    result[plant] = {'rarity': rarity, 'rating': []}

input_line = input()

while not input_line == "Exhibition":
    input_line = input_line.split()
    command = input_line[0]
    plant = input_line[1]

    if plant not in result:
        print("error")
        input_line = input()
        continue
    if command.startswith("Rate"):
        rating = int(input_line[3])
        result[plant]['rating'].append(rating)
    elif command.startswith("Update"):
        rarity = int(input_line[3])
        result[plant]['rarity'] = rarity

    elif command.startswith("Reset"):
        result[plant]['rating'] = []

    input_line = input()

print(f"Plants for the exhibition:")

for key, value in result.items():
    if len(value['rating']) > 0:
        average = sum(value['rating']) / len(value['rating'])
    else:
        average = 0
    print(f"- {key}; Rarity: {value['rarity']}; Rating: {average:.2f}")
