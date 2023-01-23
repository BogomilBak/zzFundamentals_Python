def palindrome(element):
    if element == element[::-1]:
        return True
    return False


input_line = input().split(", ")
for current_element in input_line:
    print(palindrome(current_element))
