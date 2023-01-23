input_line = [int(x) for x in input().split()]
average = sum(input_line) / len(input_line)

input_line = [x for x in input_line if x > average]

if input_line:
    input_line.sort(reverse=True)
    while len(input_line) > 5:
        input_line.pop(5)
    input_line = [str(x) for x in input_line]
    print(' '.join(input_line))

else:
    print('No')