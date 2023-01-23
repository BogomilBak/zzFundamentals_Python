input_line = input().split()
a_team = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
b_team = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
flag = False

for index in input_line:
    current_index = index.split("-")
    current_team = current_index[0]
    current_player = int(current_index[1])

    if current_team == "A" and current_player in a_team:
        a_team.remove(current_player)
    elif current_team == "B" and current_player in b_team:
        b_team.remove(current_player)

    if len(a_team) < 7 or len(b_team) < 7:
        flag = True
        break

print(f"Team A - {len(a_team)}; Team B - {len(b_team)}")
if flag:
    print("Game was terminated")
