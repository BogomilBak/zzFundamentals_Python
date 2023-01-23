# def factorial(num_1, num_2):
#     first_num = 1
#     second_num = 1
#     for digit in range(num_1, 0, -1):
#         first_num *= digit
#     for digit in range(num_2, 0, -1):
#         second_num *= digit
#     return first_num / second_num
#
import math

input_line_1 = int(input())
input_line_2 = int(input())
# print(f"{factorial(input_line_1, input_line_2):.2f}")
print(f"{math.factorial(input_line_1) / math.factorial(input_line_2):.2f}")
