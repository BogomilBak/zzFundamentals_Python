def palindrome(example_list):
    for list_index in range(len(example_list)):
        current_number = example_list[list_index]
        flag = True
        for index in range(len(example_list[list_index])):
            current_digit = current_number[index]
            backwards_digit = current_number[-1 - index]
            if current_digit != backwards_digit:
                flag = False
                break
        print(flag)


input_line = input().split(", ")
palindrome(input_line)