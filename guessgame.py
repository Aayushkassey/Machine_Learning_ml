import random

num= random.randint(1, 100)
guess= int(input("Guess a number between 1 and 100: "))
if guess == num:
    print("Congratulations! You guessed the correct number.")
else:
    print(f"Sorry, the correct number was {num}. Better luck next time!")