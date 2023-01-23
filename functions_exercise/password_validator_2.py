def password_checker(string):
    flag = True
    if not 6 <= len(string) <= 10:
        print(f"Password must be between 6 and 10 characters")
        flag = False
    digit_counter = 0
    for element in string:
        if element.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        print(f"Password must have at least 2 digits")
        flag = False
    if not string.isalnum():
        print(f"Password must consist only of letters and digits")
        flag = False
    if flag:
        print(f"Password is valid")


input_line = input()
password_checker(input_line)




