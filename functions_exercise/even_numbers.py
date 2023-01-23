def even_nums(x):
    if x % 2 == 0:
        return True
    return False


input_line = [int(x) for x in input().split()]
result = filter(even_nums, input_line)
print(list(result))