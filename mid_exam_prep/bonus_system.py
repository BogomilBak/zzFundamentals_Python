number_of_students = int(input())
total_number_lectures = int(input())
bonus = int(input())

current_maximum_bonus = 0
current_maximum_attendance = 0

for student in range(1, number_of_students + 1):
    attendances = int(input())
    maximum_bonus = attendances / total_number_lectures * (5 + bonus)
    if maximum_bonus > current_maximum_bonus:
        current_maximum_bonus = maximum_bonus
        current_maximum_attendance = attendances

print(f"Max Bonus: {round(current_maximum_bonus)}.")
print(f"The student has attended {current_maximum_attendance} lectures.")