import random
number = random.randint(1, 100)

select_level = input("Select level 'easy' or 'hard': ")

if select_level == "easy":
    trial = 10
elif select_level == "hard":
    trial = 5
else:
    print("Invalid level selected.")
    exit()

while trial > 0:
    guess = int(input("Make a guess: "))

    if guess == number:
        print("That's correct!")
        break
    elif guess > number:
        print("Too high")
    else:
        print("Too low")

    trial -= 1

    if trial > 0:
        print(f"You have {trial} attempts remaining.")
    else:
        print("You ran out of trials!")
        print(f"Correct number was {number}")
