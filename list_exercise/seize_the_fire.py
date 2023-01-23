input_line = input().split("#")
water = int(input())
effort = 0
total_fire = 0
current_water = water
result = []
for index in input_line:
    current_index = index.split(" =")
    level_fire = current_index[0]
    value_fire = int(current_index[1])
    if level_fire == "High" and 81 <= value_fire <= 125 and current_water >= value_fire:
        current_water -= value_fire
        effort += value_fire * 0.25
        result.append(value_fire)
    elif level_fire == "Medium" and 51 <= value_fire <= 80 and current_water >= value_fire:
        current_water -= value_fire
        effort += value_fire * 0.25
        result.append(value_fire)
    elif level_fire == "Low" and 1 <= value_fire <= 50 and current_water >= value_fire:
        current_water -= value_fire
        effort += value_fire * 0.25
        result.append(value_fire)
print("Cells:")
for index in range(len(result)):
    print(f" - {result[index]}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(result)}")