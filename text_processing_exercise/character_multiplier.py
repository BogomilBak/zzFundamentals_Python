input_line = input().split()

result = 0

first_num = input_line[0]
second_num = input_line[1]
smallest_num = 0
biggest_num = 0

if len(first_num) >= len(second_num):
    smallest_num = second_num
    biggest_num = first_num
else:
    smallest_num = first_num
    biggest_num = second_num

difference = len(biggest_num) - len(smallest_num)

for index in range(len(smallest_num)):
    result += ord(smallest_num[index]) * ord(biggest_num[index])

for index in range(difference):
    result += ord(biggest_num[-1 -(index)])


print(result)
