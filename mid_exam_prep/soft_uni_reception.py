import math

first_per_hour = int(input())
second_per_hour = int(input())
third_per_hour = int(input())
student_count = int(input())

total_capacity = first_per_hour + second_per_hour + third_per_hour
time_needed = math.ceil(student_count / total_capacity)
break_time = time_needed / 3
time_needed += break_time
time_needed = int(time_needed)

print(f"Time needed: {time_needed}h.")