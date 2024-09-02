import random

dice_num = int(input("How many dice do you want to roll: "))
sum = 0

for i in range(dice_num):
    roll = random.randint(1, 6)
    sum = roll + sum

print(f"The sum of all {dice_num} dices is {sum}")