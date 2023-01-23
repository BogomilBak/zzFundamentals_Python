input_line = [int(x) for x in input().split()]
happy = int(input())
happyness_1 = list(map(lambda x: x * happy, input_line))
filtered = list(filter(lambda x: x >= sum(happyness_1) / len(happyness_1), happyness_1))


if len(filtered) >= len(happyness_1) / 2:
    print(f"Score: {len(filtered)}/{len(happyness_1)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(happyness_1)}. Employees are not happy!")
