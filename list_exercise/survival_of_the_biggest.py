input_line = input().split()
count = int(input())

input_line = [int(x) for x in input_line]

for i in range(count):
    input_line.remove(min(input_line))

input_line = [str(x) for x in input_line]

print(", ".join(input_line))