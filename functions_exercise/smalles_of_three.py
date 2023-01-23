def smallest_calculator(num_1, num_2, num_3):
    if num_1 <= num_3 and num_1 <= num_2:
        return num_1
    elif num_2 <= num_1 and num_2 <= num_3:
        return num_2
    elif num_3 <= num_1 and num_3 <= num_2:
        return num_3


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(smallest_calculator(first_num, second_num, third_num))

