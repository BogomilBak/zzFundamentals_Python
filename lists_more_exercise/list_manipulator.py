given_list = [int(x) for x in input().split(" ")]
input_line = input().split()
exchange_list = []
odd_element = 2
even_element = 1
counter_1 = 0
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
        if given_index > len(given_list):
            print(f"Invalid index")
        else:
            counter = 0
            while counter - 1 < given_index:
                    exchange_list.append(given_list[0])
                    given_list.pop(0)
                    counter += 1
            counter = 0
            while counter < given_index + 1:
                given_list.append(exchange_list[0])
                exchange_list.pop(0)
                counter += 1
    elif command == "max" and input_line[1] == "even":
        if even_element != 1:
            max_number = max([x for x in given_list if x % 2 == 0])
            print(f"{given_list.index(max_number)}")
        else:
            print(f"No matches")
    elif command == "max" and input_line[1] == "odd":
        if odd_element != 2:
            max_number = max([x for x in given_list if x % 2 != 0])
            print(f"{given_list.index(max_number)}")
        else:
            print(f"No matches")
    elif command == "min" and input_line[1] == "even":
        if even_element != 1:
            min_number = min([x for x in given_list if x % 2 == 0])
            print(f"{given_list.index(min_number)}")
        else:
            print(f"No matches")
    elif command == "min" and input_line[1] == "odd":
        if odd_element != 2:
            min_number = min([x for x in given_list if x % 2 == 0])
            if 1 in given_list:
                print(f"{given_list.index(1)}")
            else:
                print(f"{given_list.index(min_number)}")
        else:
            print(f"No matches")

    elif command == "first":
        if input_line[2] == "even":
            if int(input_line[1]) > len(given_list):
                print("Invalid count")
            else:
                for index in given_list:
                    if index % 2 == 0:
                        exchange_list.append(index)
                        counter_1 += 1
                    if counter_1 == int(input_line[1]):
                        flag = True
                        print(exchange_list)
                        exchange_list = []
                        counter_1 = 0
                        break
                if counter_1 < int(input_line[1]) and flag == False:
                    print(exchange_list)
                    exchange_list = []

        elif input_line[2] == "odd":
            if int(input_line[1]) > len(given_list):
                print("Invalid count")
            else:
                for index in given_list:
                    if index % 2 != 0:
                        exchange_list.append(index)
                        counter_1 += 1
                    if counter_1 == int(input_line[1]):
                        flag = True
                        print(exchange_list)
                        exchange_list = []
                        counter_1 = 0
                        break
                if counter_1 < int(input_line[1]) and flag == False:
                    print(exchange_list)
                    exchange_list = []
    elif command == "last":
        if input_line[2] == "even":
            if int(input_line[1]) > len(given_list):
                print("Invalid count")
            else:
                for index in reversed(given_list):
                    if index % 2 == 0:
                        exchange_list.append(index)
                        counter_1 += 1
                    if counter_1 == int(input_line[1]):
                        flag = True
                        print(exchange_list)
                        exchange_list = []
                        counter_1 = 0
                        break
                if counter_1 < int(input_line[1]) and flag == False:
                    print(exchange_list)
                    exchange_list = []
        elif input_line[2] == "odd":
            if int(input_line[1]) > len(given_list):
                print("Invalid count")
            else:
                for index in reversed(given_list):
                    if index % 2 != 0:
                        exchange_list.append(index)
                        counter_1 += 1
                    if counter_1 == int(input_line[1]):
                        flag = True
                        print(exchange_list)
                        exchange_list = []
                        counter_1 = 0
                        break
                if counter_1 < int(input_line[1]) and flag == False:
                    print(exchange_list)
                    exchange_list = []

    input_line = input().split()

print(given_list)
