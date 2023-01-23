def password_checker(string):
    flag = True
    flag_1 = True
    if not 6 <= len(string) <= 10:
        print(f"Password must be between 6 and 10 characters")
        flag = False
    digit_counter = 0
    for index in range(len(string)):
        current_digit = ord(string[index])
        if not 65 <= current_digit <= 90 and not 97 <= current_digit <= 122 and not 48 <= current_digit <= 57 and flag_1 == True:
            print(f"Password must consist only of letters and digits")
            flag = False
            flag_1 = False
            break
        if 48 <= current_digit <= 57:
            digit_counter += 1
    if digit_counter < 2:
        print(f"Password must have at least 2 digits")
        flag = False
    if flag:
        print(f"Password is valid")


input_line = input()
password_checker(input_line)




