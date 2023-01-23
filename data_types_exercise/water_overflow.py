input_lines = int(input())
current = 0
for i in range(input_lines):
    session = int(input())
    if session + current > 255:
        print("Insufficient capacity!")
        continue
    current += session

print(current)