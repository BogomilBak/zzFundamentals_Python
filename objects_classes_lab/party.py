class Party:
    def __init__(self):
        self.people = []


people = Party()

while True:
    input_line = input()
    if input_line == "End":
        break
    people.people.append(input_line)

print(f"Going: {', '.join(people.people)}")
print(f"Total: {len(people.people)}")
