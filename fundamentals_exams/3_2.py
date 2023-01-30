import re

input_line = input()

pattern_emoji = r"(?<=(::|\*\*))[A-Z][a-z][a-z]+(?=\1)"
pattern_emoji_full = r"(::|\*\*)[A-Z][a-z][a-z]+\1"
pattern_thr = r"\d"
result = []
threshold = 1

emoji = [x.group() for x in re.finditer(pattern_emoji, input_line)]
emoji_full = [x.group() for x in re.finditer(pattern_emoji_full, input_line)]

thr = [int(x) for x in re.findall(pattern_thr, input_line)]

for element in thr:
    threshold *= element

for element in range(len(emoji)):
    sum_element = sum([ord(x) for x in emoji[element]])
    if sum_element >= threshold:
        result.append(emoji_full[element])

print(f"Cool threshold: {threshold}")
print(f"{len(emoji_full)} emojis found in the text. The cool ones are:")

for element in result:
    print(element)
