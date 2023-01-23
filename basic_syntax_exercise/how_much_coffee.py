coffees = 0

while True:
    input_line = input()
    if input_line == "End" or input_line == "END":
        break
    if input_line in ["coding", "dog", "cat", "movie"]:
        coffees += 1
    elif input_line in ["CODING", "DOG", "CAT", "MOVIE"]:
        coffees += 2
if coffees <= 5:
    print(coffees)
else:
    print("You need extra sleep")