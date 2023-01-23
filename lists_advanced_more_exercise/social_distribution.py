input_line = list(map(int, input().split(", ")))
minimum = int(input())
wealthiest = max(input_line)
rich_index = input_line.index(wealthiest)
to_take = 0
result = []

if len(input_line) * minimum <= sum(input_line):
    for index in range(len(input_line)):
        if input_line[index] < minimum:
            to_take += minimum - input_line[index]
            input_line[index] = minimum
    while to_take > 0:
        input_line[rich_index] -= 1
        to_take -= 1
        wealthiest = max(input_line)
        rich_index = input_line.index(wealthiest)

    print(input_line)
else:
    print('No equal distribution possible')


