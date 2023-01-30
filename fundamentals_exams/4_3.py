lines = int(input())

result = {}

for _ in range(lines):
    car, distance, fuel = input().split("|")
    distance = int(distance)
    fuel = int(fuel)
    result[car] = {'distance': distance, 'fuel': fuel}

input_line = input()

while not input_line == "Stop":
    input_line = input_line.split(" : ")
    command = input_line[0]
    car = input_line[1]

    if command == "Drive":
        distance = int(input_line[2])
        fuel = int(input_line[3])
        if fuel <= result[car]['fuel']:
            result[car]['distance'] += distance
            result[car]['fuel'] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")

        if result[car]['distance'] >= 100000:
            print(f"Time to sell the {car}!")
            del result[car]
    elif command == "Refuel":
        fuel = int(input_line[2])
        if fuel + result[car]['fuel'] > 75:
            fuelled = 75 - result[car]['fuel']
            result[car]['fuel'] = 75
        else:
            result[car]['fuel'] += fuel
            fuelled = fuel

        print(f"{car} refueled with {fuelled} liters")

    elif command == "Revert":
        km = int(input_line[2])
        result[car]['distance'] -= km

        if result[car]['distance'] >= 10000:
            print(f"{car} mileage decreased by {km} kilometers")

        else:
            result[car]['distance'] = 10000

    input_line = input()

for key, value in result.items():
    print(f"{key} -> Mileage: {value['distance']} kms, Fuel in the tank: {value['fuel']} lt.")