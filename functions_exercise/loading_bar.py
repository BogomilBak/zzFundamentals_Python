def loading_bar(num_1):
    example_list = ["."] * 10
    replacements = int(num_1 / 10)
    for i in range(replacements):
        example_list[i] = "%"
    return example_list


input_line = int(input())
result = [''.join(loading_bar(input_line))]
if input_line < 100:
    print(f"{input_line}% [{''.join(result)}] ")
    print(f"Still loading...")
else:
    print(f"100% Complete!")
    print(f"[{''.join(''.join(loading_bar(input_line)))}]")
