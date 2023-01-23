input_line = [x for x in input().split() if x == x[::-1]]
searched = input()
print(input_line)
print(f"Found palindrome {input_line.count(searched)} times")
