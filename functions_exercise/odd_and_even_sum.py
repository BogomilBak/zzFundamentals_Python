def example(num_1):
    odd_sum = 0
    even_sum = 0
    for index in range(len(num_1)):
        current_number = int(num_1[index])
        if current_number % 2 == 0:
            even_sum += current_number
        else:
            odd_sum += current_number
    return [odd_sum, even_sum]


input_line = input()
print(f"Odd sum = {example(input_line)[0]}, Even sum = {example(input_line)[1]}")
