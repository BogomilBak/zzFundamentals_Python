input_line = input()

data = []
current_word = ""

if "," in input_line:
    for element in range(len(input_line)):
        if input_line[element] == "," or input_line[element] == " " or element == len(input_line) -1:
            if len(current_word) > 0:
                data.append(current_word)
            current_word = ""
        else:
            current_word += input_line[element]

        if element == len(input_line) - 2:
            current_word += input_line[element + 1]

    for element in range(len(data)):
        if not len(data[element]) == 20:
            print('invalid ticket')
            continue
        current_ticket = '"' + data[element] + '"'
        left_side = 0
        right_side = 0
        winning_symbol = ""
        for index in range(10):
            if data[element][index] in ['@', '#', '$', '^']:
                left_side += 1
                if left_side == 6 or right_side == 6:
                    winning_symbol = data[element][index]

            else:
                if 0 < left_side < 6:
                    left_side = 0

            if data[element][index + 10] in ['@', '#', '$', '^']:
                right_side += 1
                if left_side == 6 or right_side == 6:
                    winning_symbol = data[element][index]

            else:
                if 0 < right_side < 6:
                    right_side = 0

        match_count = min(left_side, right_side)

        if left_side == 10 and right_side == 10:
            print(f"ticket {current_ticket} - 10{winning_symbol} Jackpot!")

        elif left_side >= 6 and right_side >= 6:
            print(f"ticket {current_ticket} - {match_count}{winning_symbol}")

        else:
            print(f"ticket {current_ticket} - no match")

else:

    if not len(input_line) == 20:
        print('invalid ticket')
    else:
        current_ticket = '"' + input_line + '"'
        left_side = 0
        right_side = 0
        winning_symbol = ""
        for index in range(10):
            if input_line[index] in ['@', '#', '$', '^']:
                left_side += 1
                if left_side == 6 or right_side == 6:
                    winning_symbol = input_line[index]

            else:
                if 0 < left_side < 6:
                    left_side = 0

            if input_line[index + 10] in ['@', '#', '$', '^']:
                right_side += 1
                if left_side == 6 or right_side == 6:
                    winning_symbol = input_line[index]

            else:
                if 0 < right_side < 6:
                    right_side = 0

        match_count = min(left_side, right_side)

        if left_side == 10 and right_side == 10:
            print(f"ticket {current_ticket} - 10{winning_symbol} Jackpot!")

        elif left_side >= 6 and right_side >= 6:
            print(f"ticket {current_ticket} - {match_count}{winning_symbol}")

        else:
            print(f"ticket {current_ticket} - no match")

