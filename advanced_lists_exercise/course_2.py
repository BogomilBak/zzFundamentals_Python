course = input().split(", ")

while True:
    command = input().split(":")
    if "course start" in command:
        break

    if command[0] == "Add":
        if command[1] not in course:
            course.append(command[1])
    elif command[0] == "Insert":
        if command[1] not in course:
            course.insert(int(command[2]), command[1])
    elif command[0] == "Remove":
        if command[1] in course:
            course.remove(command[1])
        if f"{command[1]}-Exercise" in course:
            course.remove(f"{command[1]}-Exercise")
    elif command[0] == "Swap":
        if command[1] in course and command[2] in course:
            a, b = course.index(command[1]), course.index(command[2])
            course[a], course[b] = course[b], course[a]
            if f"{command[1]}-Exercise" in course and f"{command[2]}-Exercise" not in course:
                course.insert(course.index(f"{command[1]}-Exercise"), course.pop(course.index(f"{command[1]}-Exercise")))
            elif f"{command[1]}-Exercise" not in course and f"{command[2]}-Exercise" in course:
                course.insert(course.index(f"{command[2]}-Exercise"), course.pop(course.index(f"{command[2]}-Exercise")))
            elif f"{command[1]}-Exercise" in course and f"{command[2]}-Exercise" in course:
                b, d = course.index(f"{command[1]}-Exercise"), course.index(f"{command[2]}-Exercise")
                course[b], course[d] = course[d], course[b]
    elif command[0] == "Exercise":
        if command[1] in course:
            index = course.index(command[1]) + 1
            course.insert(index, f"{command[1]}-Exercise")
        else:
            course.append(command[1])
            course.append(f"{command[1]}-Exercise")
for i in range(len(course)):
    course[i] = f"{i + 1}." + course[i]
print('\n'.join(course))
