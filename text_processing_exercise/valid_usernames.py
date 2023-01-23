input_line = input().split(", ")

result = []

for word in input_line:
    if word.isalpha() or word.isdigit() or word.isalnum() or '-' in word or '_' in word:
        if 2 < len(word) < 17:
            result.append(word)

for element in result:
    print(element)
