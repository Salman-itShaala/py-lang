import random

# 🎮 Mini Game: Number Guessing Game

number = random.randint(1, 100)

print(number)

shouldContinue = True

while shouldContinue:
    guess = int(input("Guess the number [secret number is 1 to 100]"))

    diff = (number - guess)

    if diff < 0:
        diff = diff * -1

    if diff == 0:
        print("Wow you guessed it, congo 🔥")
        shouldContinue = False
    elif diff <= 5:
        print("you are too close")
    elif diff <= 10:
        print("You are close")
    elif diff <= 20:
        print("You're somewhere close")
    else:
        print("You can do it, try harder n try changing range")


# things to improve

# 🔧 Tiny Improvement (Optional):
# This part:

# python
# Copy
# Edit
# diff = (number - guess)
# if diff < 0:
#     diff = diff * -1
# Can be written as:

# python
# Copy
# Edit
# diff = abs(number - guess)
# The abs() function returns the absolute value, so it’s cleaner and more readable.

# 🌈 Bonus Ideas if You Want to Expand:
# Add a guess counter and show how many attempts were made

# Add a score system: fewer guesses = higher score

# Add difficulty levels (e.g., Easy: 1–50, Hard: 1–200)

# Add play again logic (input("Play again? y/n"))