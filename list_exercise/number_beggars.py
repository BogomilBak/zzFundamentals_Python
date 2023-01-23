input_line = [int(x) for x in input().split(", ")]
beggars_count = int(input())
result = [0] * beggars_count
counter = 0
for index in input_line:
    result[counter] += index
    counter += 1
    if counter == beggars_count:
        counter = 0
print(result)