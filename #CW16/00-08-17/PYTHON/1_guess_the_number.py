import random


computers_choice = random.choice(range(1, 101))

chances = 5
used_chances = 0

while True:
    user_input = int(input("Enter your guess: "))

    if used_chances < 5:

        if user_input == computers_choice:
            print("WON!")
            break

        elif user_input > computers_choice:
            print("bigger!")
            used_chances += 1

        else:
            print("less!")
            used_chances += 1

    else:
        print("lost!")
        break
