amount = int(input())

database = {}

for _ in range(amount):
    input_line = input().split()

    command = input_line[0]
    name = input_line[1]

    if command == "register":
        license_plate = input_line[2]
        if name not in database:
            database[name] = license_plate
            print(f"{name} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {database[name]}")
    elif command == "unregister":
        if name not in database:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del database[name]

for key, value in database.items():
    print(f"{key} => {value}")
