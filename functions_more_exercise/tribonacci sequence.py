def tribonacci(num):
    temp_list = []
    counter = 0
    for i in range(1, num + 1):
        if counter < 3:
            if counter == 0 or counter == 1:
                temp_list.append(1)
                counter += 1
            elif counter == 2:
                temp_list.append(2)
                counter += 1
        else:
            backwards_list = temp_list[::-1]
            backwards_list = backwards_list[:3]
            current_num = sum(backwards_list)
            temp_list.append(current_num)

    return temp_list


input_line = int(input())
result = tribonacci(input_line)
for x in result:
    print(x, end=" ")
