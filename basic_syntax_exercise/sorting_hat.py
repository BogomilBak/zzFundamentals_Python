while True:
    input_line = input()
    if input_line == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    if input_line == "Voldemort":
        print("You must not speak of that name!")
        break
    if len(input_line) < 5:
        print(f"{input_line} goes to Gryffindor.")
    elif len(input_line) == 5:
        print(f"{input_line} goes to Slytherin.")
    elif len(input_line) == 6:
        print(f"{input_line} goes to Ravenclaw.")
    elif len(input_line) > 6:
        print(f"{input_line} goes to Hufflepuff.")