input_line = input()
result = {}


while "-" in input_line:
    contact, number = input_line.split("-")
    if contact not in result:
        result[contact] = ""
    result[contact] = number

    input_line = input()

for _ in range(int(input_line)):
    contact = input()
    if contact in result:
        print(f"{contact} -> {result[contact]}")

    else:
        print(f"Contact {contact} does not exist.")
