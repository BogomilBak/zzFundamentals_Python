password = input()

input_line = input()

while not input_line == "Done":

    if input_line.startswith("TakeOdd"):
        new_password = ""
        for element in range(len(password)):
            if not element % 2 == 0:
                new_password += password[element]

        password = new_password
        print(password)
    elif input_line.startswith("Cut"):
        command, index, length = input_line.split()
        index = int(index)
        length = int(length)
        to_remove = password[index: index + length]
        password = password.replace(to_remove, "", 1)
        print(password)
    elif input_line.startswith("Substitute"):
        command, substring, substitute = input_line.split()
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    input_line = input()

print(f"Your password is: {password}")
