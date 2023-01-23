input_line = int(input())
result = {}

for element in range(input_line):
    word = input()
    synonym = input()
    if word not in result:
        result[word] = []
    result[word].append(synonym)

for key, element in result.items():
    print(f"{key} - {', '.join(element)}")
