input_line = int(input())
wall = 0
kate_found = False
bust = False
moves_needed = 0
kate_move_points = []
for maze in range(1, input_line + 1):
    current_map = input()
    if current_map == "######":
        wall += 1
    if "k" in current_map:
        kate_found = True
        if wall > 1:
            wall = 1
    if kate_found and wall == 2:
        print(f"Kate cannot get out")
        break
    if kate_found:
        if "k" in current_map:
            kate_index = current_map.index("k")
            if current_map[:kate_index] > current_map[kate_index:]:
                for index in current_map[kate_index:]:
                    if index == " ":
                        moves_needed += 1
                        current_index = current_map.index(index)
                        kate_move_points.append(current_index)

            elif current_map[:kate_index] < current_map[kate_index:]:
                for index in current_map[:kate_index]:
                    if index == " ":
                        moves_needed += 1
                        current_index = current_map.index(index)
                        kate_move_points.append(current_index)

        else:
            for index in current_map:
                if index == " ":
                    moves_needed += 1

if kate_found and wall < 2:
    print(f"Kate got out in {moves_needed + 1} moves")


