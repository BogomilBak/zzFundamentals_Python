first_line = [int(x) for x in input().split()]
second_line = [int(x) for x in input().split()]
third_line = [int(x) for x in input().split()]

if first_line[0] == second_line[0] == third_line[0] and not first_line[0] == 0:
    if first_line[0] == 1:
        print("First player won")
    else:
        print("Second player won")
elif first_line[1] == second_line[1] == third_line[1] and not first_line[0] == 0:
    if first_line[1] == 1:
        print("First player won")
    else:
        print("Second player won")
elif first_line[2] == second_line[2] == third_line[2] and not first_line[0] == 0:
    if first_line[2] == 1:
        print("First player won")
    else:
        print("Second player won")
elif first_line[0] == first_line[1] == first_line[2] and not first_line[0] == 0:
    if first_line[0] == 1:
        print("First player won")
    else:
        print("Second player won")
elif second_line[0] == second_line[1] == second_line[2] and not second_line[0] == 0:
    if second_line[0] == 1:
        print("First player won")
    else:
        print("Second player won")
elif third_line[0] == third_line[1] == third_line[2] and not third_line[0] == 0:
    if third_line[0] == 1:
        print("First player won")
    else:
        print("Second player won")
elif first_line[0] == second_line[1] == third_line[2] and not first_line[0] == 0:
    if first_line[0] == 1:
        print("First player won")
    else:
        print("Second player won")
elif first_line[2] == second_line[1] == third_line[0] and not first_line[2] == 0:
    if first_line[2] == 1:
        print("First player won")
    else:
        print("Second player won")
else:
    print("Draw!")