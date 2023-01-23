input_line_1 = list(map(int, input().split(", ")))
res = map(lambda x: x if input_line_1[x] % 2 == 0 else 'no', range(len(input_line_1)))
res_1 = list(filter(lambda a: not a == "no", res))
print(res_1)