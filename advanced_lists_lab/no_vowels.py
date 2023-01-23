vowels = ["a", "o", "u", "e", "i"]
input_line = input()
filtered = [ch for ch in input_line if ch.lower() not in vowels]
print("".join(filtered))
