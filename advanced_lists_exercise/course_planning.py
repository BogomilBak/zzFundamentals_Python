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
            if course.count(f"{command[1]}-Exercise") > 0 and course.count(f"{command[2]}-Exercise") == 0:
                a, c = course.index(command[1]), course.index(command[2])
                course[a], course[c] = course[c], course[a]
                course.insert(course.index(command[1]) + 1, course.pop(course.index(f"{command[1]}-Exercise")))
            elif course.count(f"{command[1]}-Exercise") == 0 and course.count(f"{command[2]}-Exercise") > 0:
                a, c = course.index(command[1]), course.index(command[2])
                course[a], course[c] = course[c], course[a]
                course.insert(course.index(command[2]) + 1, course.pop(course.index(f"{command[2]}-Exercise")))
            elif course.count(f"{command[1]}-Exercise") > 0 and course.count(f"{command[2]}-Exercise") > 0:
                a, b, c, d = course.index(command[1]), course.index(f"{command[1]}-Exercise"), course.index(command[2]), course.index(f"{command[2]}-Exercise")
                course[a], course[b], course[c], course[d] = course[c], course[d], course[a], course[b]
            else:
                a, b = course.index(command[1]), course.index(command[2])
                course[a], course[b] = course[b], course[a]
    elif command[0] == "Exercise":
        if command[1] in course:
            index = course.index(command[1]) + 1
            course.insert(index, f"{command[1]}-Exercise")
        else:
            course.append(command[1])
            course.append(f"{command[1]}-Exercise")
for index, value in enumerate(course):
    print(f"{index + 1}.{value}")

