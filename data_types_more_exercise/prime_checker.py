number = int(input())
counter = 0
for current_number in range(1, number + 1):
    if number % current_number == 0:
        counter += 1

if counter == 2:
    print("True")
else:
    print("False")