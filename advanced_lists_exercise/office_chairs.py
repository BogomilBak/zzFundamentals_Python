rooms = int(input())
flag = True
free_chairs = 0
for i in range(1, rooms + 1):
    input_line = input().split()
    difference = abs(int(input_line[1]) - len(input_line[0]))
    if len(input_line[0]) < int(input_line[1]):
        print(f"{difference} more chairs needed in room {i}")
        flag = False
    else:
        free_chairs += difference
if flag:
    print(f"Game On, {free_chairs} free chairs left")
