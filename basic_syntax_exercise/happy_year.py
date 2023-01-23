year = int(input())
while True:
    year += 1
    year = str(year)
    counter = 0
    for a in year:
        for b in year:
            if a == b:
                counter += 1
    if counter == len(year):
        print(year)
        break
    year = int(year)