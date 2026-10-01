import random as r


amount = int(input("Enter the amount of numbers you want to guess to: "))
number = r.randint(1, amount)
guess_amount = 1
guess = int(input("\nEnter your first guess: "))

while(number != guess):
    if guess < number:
        print("\nToo small")
    if guess > number:
        print("\nToo big")

    guess = int(input("Guess again: "))
    guess_amount += 1

print("\nYou win")
print(f"You got it in {guess_amount} guesses")