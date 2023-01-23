cards = input().split()
shuffles = int(input())

half_cards = len(cards) // 2

for i in range(shuffles):

    left_half = cards[0:half_cards]
    right_half = cards[half_cards:]

    faro_shuffle = []

    for j in range(half_cards):
        faro_shuffle.append(left_half[j])
        faro_shuffle.append(right_half[j])

    cards = faro_shuffle

print(cards)