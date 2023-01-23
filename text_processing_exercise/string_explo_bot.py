def process_string(s):
    strength = 0
    final_string = ""
    for i, c in enumerate(s):
        if c == ">":
            strength += int(s[i+1])
            final_string += c
        elif strength > 0:
            strength -= 1
        else:
            final_string += c
    print(final_string)

s = input()
process_string(s)

