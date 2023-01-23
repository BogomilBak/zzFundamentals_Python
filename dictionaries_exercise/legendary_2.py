result = {}
value = 0
flag = True

input_line = input().split()
while flag:

    for element in range(1, len(input_line) + 1):
        if element % 2 == 0:
            key = input_line[element - 1].lower()
            if key not in result:
                result[key] = 0
            result[key] += value
        else:
            value = int(input_line[element - 1])

        if "shards" in result and result['shards'] >= 250:
            result['shards'] -= 250
            print(f"Shadowmourne obtained!")
            flag = False
            break
        elif "fragments" in result and result['fragments'] >= 250:
            result['fragments'] -= 250
            print(f"Valanyr obtained!")
            flag = False
            break
        elif "motes" in result and result['motes'] >= 250:
            result['motes'] -= 250
            print(f"Dragonwrath obtained!")
            flag = False
            break

    if not flag:
        break

    input_line = input().split()

if "shards" in result:
    print(f"shards: {result['shards']}")
    del result['shards']
else:
    print(f"shards: 0")
if "fragments" in result:
    print(f"fragments: {result['fragments']}")
    del result['fragments']
else:
    print(f"fragments: 0")
if "motes" in result:
    print(f"motes: {result['motes']}")
    del result['motes']
else:
    print(f"motes: 0")

for key, value in result.items():
    print(f"{key}: {value}")