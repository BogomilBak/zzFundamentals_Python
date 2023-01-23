given_list = [int(x) for x in input().split(" ")]
input_line = input().split()
exchange_list = []
odd_element = 0
even_element = 0
counter_1 = 0
flag = False
for element in given_list:
    if element % 2 == 0:
        even_element = element
    elif element % 2 != 0:
        odd_element = element

while not "end" in input_line:
    flag = False
    command = input_line[0]
    if command == "exchange":
        given_index = int(input_line[1])
        counter = 0
        while counter < given_index + 1:
                exchange_list.append(given_list[0])
                given_list.pop(0)
                counter += 1
        counter = 0
        while counter < given_index + 1:
            given_list.append(exchange_list[0])
            exchange_list.pop(0)
            counter += 1
