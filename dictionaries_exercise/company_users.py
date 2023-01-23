input_line = input()

result = {}

while not input_line == "End":
    company, worker_id = input_line.split(" -> ")
    if company not in result:
        result[company] = []
    if worker_id not in result[company]:
        result[company].append(worker_id)

    input_line = input()

for key, value in result.items():
    print(f"{key}")
    for index in value:
        print(f"-- {index}")
