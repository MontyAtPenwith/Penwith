# get name and age
name = input("What is your name?: ")
age = int(input(f"How old are you {name}?: "))

# calculate
birth_year = 2026 - age

# print
print(f"\nYour name is {name}!")
print(f"You are {age} years old!")
print(f"You were born in {birth_year}!")