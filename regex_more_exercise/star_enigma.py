import re

letters = ['S', 'T', 'A', 'R']

lines = int(input())
attacked_planets = []
destroyed_planets = []

for _ in range(lines):
    count = 0
    decrypted = ""
    input_line = input()
    for letter in letters:
        pattern = fr"[{letter}]"
        match = re.findall(pattern, input_line, re.IGNORECASE)
        if match:
            count += len(match)

    for letter in range(len(input_line)):
        dec_letter = chr(ord(input_line[letter]) - count)
        decrypted += dec_letter

    pattern = r"(?<=@)(?P<name>[A-Za-z]+)[^|@!:>-]*?:(?P<population>[0-9]+)[^|@!:>-]*?!(?P<attack>(A|D))![^|@!:>-]*?->(?P<soldiers>[0-9]+)"
    semi_result = [x.groupdict() for x in re.finditer(pattern, decrypted)]
    if semi_result:
        if semi_result[0]['attack'] == 'A':
            attacked_planets.append(semi_result[0]['name'])
        elif semi_result[0]['attack'] == 'D':
            destroyed_planets.append(semi_result[0]['name'])

sorted_attacked_planets = sorted(attacked_planets)
sorted_destroyed_planets = sorted(destroyed_planets)

print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted_attacked_planets:
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in sorted_destroyed_planets:
    print(f"-> {planet}")
