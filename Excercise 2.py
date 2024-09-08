num_list = []

while True:
    user_input = input("Enter a number (or press Enter to finish): ")

    if user_input == "":
        break

    try:
        num = int(user_input)
        num_list.append(num)
    except ValueError:
        print("Please enter a valid number.")

num_list.sort(reverse=True)
top_five_numbers = num_list[:5]

print("The five greatest numbers are:")
for nums in top_five_numbers:
    print(nums)