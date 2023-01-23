def perfect(num_1):
    current_sum = 0
    for i in range(1, num_1):
        if num_1 % i == 0:
            current_sum += i
    if current_sum == num_1:
        return "We have a perfect number!"
    return "It's not so perfect."


input_line = int(input())
print(perfect(input_line))
