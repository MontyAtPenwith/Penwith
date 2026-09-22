from ut import cmd
cmd.cls()

accompanied = False
age = int(input("Enter your age: "))

if age > 5 and age < 16:
    with_adult = input("Are you accompanied?: ")
    with_adult = with_adult.lower()
    if with_adult == "yes" or with_adult == "y" or with_adult == "true":
        accompanied = True

if age <= 0:
    print("You haven't been born yet!")
    cmd.exit()

if age < 5:
    price = 0

elif age < 16:
    price = 15
    if accompanied:
        price -= 5

elif age < 65:
    price = 25

elif age >= 65:
    price = 18

else:
    print("Enter a valid age")

print(f"Your ticket price is £{price}")