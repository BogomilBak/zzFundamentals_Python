dwarfs = {}
while True:
    command = input()
    if command == "Once upon a time":
        break
    command = command.split(" <:> ")
    name = command[0]
    hat_color = command[1]
    physics = int(command[2])
    if name in dwarfs:
        if dwarfs[name]["hat_color"] == hat_color:
            if dwarfs[name]["physics"] < physics:
                dwarfs[name]["physics"] = physics
        else:
            dwarfs[name + hat_color] = {"hat_color": hat_color, "physics": physics}
    else:
        dwarfs[name] = {"hat_color": hat_color, "physics": physics}

dwarfs = dict(sorted(dwarfs.items(), key=lambda x: (-x[1]["physics"], -x[1]["hat_color"])))
for dwarf in dwarfs:
    print(f"({dwarfs[dwarf]['hat_color']}) {dwarf.split(dwarfs[dwarf]['hat_color'])[0]} <-> {dwarfs[dwarf]['physics']}")
