input_line = list(map(int, input().split(", ")))
minimum = int(input())
wealthiest = max(input_line)
rich_index = input_line.index(wealthiest)


if len(input_line) * minimum <= sum(input_line):
    while not min(input_line) == minimum:
        poorest = min(input_line)
        poorest_index = input_line.index(poorest)
        wealthiest = max(input_line)
        rich_index = input_line.index(wealthiest)
        to_take = minimum - input_line[poorest_index]
        input_line[poorest_index] = minimum
        input_line[rich_index] -= to_take

    print(input_line)
else:
    print('No equal distribution possible')


