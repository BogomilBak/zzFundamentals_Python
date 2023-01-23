input_line = input()

result = {}

while not input_line == "Lumpawaroo":
    flag = True
    flag_1 = True
    if "|" in input_line:
        force_side, force_user = input_line.split(" | ")
        if force_side not in result:
            result[force_side] = []

        for key, value in result.items():
            for element in value:
                if element == force_user:
                    flag_1 = False

        if flag_1:
            result[force_side].append(force_user)

    else:
        force_user, force_side = input_line.split(" -> ")

        for key, value in result.items():
            if force_user in value and flag:
                if key != force_side:
                    result[key].remove(force_user)
                    break
                else:
                    result[key].remove(force_user)
                    for key_two, value_two in result.items():
                        if key_two != key:
                            result[key_two].append(force_user)
                            flag = False
                            print(f"{force_user} joins the {key_two} side!")
                            break

        if force_side in result and force_user not in result.items() and flag:
            result[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")

        elif force_side not in result and force_user not in result.items() and flag:
            result[force_side] = []
            result[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")

    input_line = input()

for key, value in result.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for element in value:
            print(f"! {element}")
