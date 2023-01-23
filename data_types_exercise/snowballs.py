number_of_snowballs = int(input())

current_best_value = 0
current_best_weight = 0
current_best_time = 0
current_best_quality = 0


for snowball in range(1, number_of_snowballs + 1):
    weight_of_snowballs = int(input())
    time_to_make_snowballs = int(input())
    quality_of_snowballs = int(input())

    value = (weight_of_snowballs / time_to_make_snowballs) ** quality_of_snowballs
    if value > current_best_value:
        current_best_value = int(value)
        current_best_weight = weight_of_snowballs
        current_best_time = time_to_make_snowballs
        current_best_quality = quality_of_snowballs

print(f"{current_best_weight} : {current_best_time} = {current_best_value} ({int(current_best_quality)})")