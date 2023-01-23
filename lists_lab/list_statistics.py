number_lines = int(input())
positive_list = []
negative_list = []

for _ in range(number_lines):
    input_line = int(input())
    if input_line >= 0:
        positive_list.append(input_line)
    else:
        negative_list.append(input_line)

print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {sum(negative_list)}")

