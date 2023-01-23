winning_symbols = ['@', '#', '$', '^']


def is_jackpot(ticket):
    for symbol in winning_symbols:
        if symbol * 20 in ticket:
            print(f'ticket "{ticket}" - 10{symbol} Jackpot!')
            return True
    return False


def is_winning(ticket):
    left_side = ticket[:10]
    right_side = ticket[10:]
    match_length = 0
    for symbol in winning_symbols:
        if symbol * 6 in left_side and symbol * 6 in right_side:
            match_length = 6
        if symbol * 7 in left_side and symbol * 7 in right_side:
            match_length = 7
        if symbol * 8 in left_side and symbol * 8 in right_side:
            match_length = 8
        if symbol * 9 in left_side and symbol * 9 in right_side:
            match_length = 9

        if match_length >= 6:
            print(f'ticket "{ticket}" - {match_length}{symbol}')
            return True
    return False


input_line = [x.strip() for x in input().split(",")]

for ticket in input_line:
    if not len(ticket) == 20:
        print('invalid ticket')
        continue

    if is_jackpot(ticket):
        continue

    if is_winning(ticket):
        continue

    else:
        print(f'ticket "{ticket}" - no match')
