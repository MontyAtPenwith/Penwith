
def get_monthly_fee(age: int) -> int:

    if age < 18:
        price = 18
    elif age >=65:
        price = 20
    elif age >= 18 and age <= 64:
        price = 30

    else:
        print("Return a valid age")
        price = 0

    return price


def get_total(age: int, months: int) -> float:

    price = get_monthly_fee(age)
    subtotal = price * months

    if months >= 12:
        total = subtotal - (subtotal/10)
    else:
        total = subtotal

    return total



age = int(input("Enter how old are you (years): "))
while age <= 0 or age > 100:
    age = int(input("You must be between 1 and 100 to have a membership: "))

months = int(input("Enter how many months you want to sign up for (1-24): "))
while months <= 0 or months > 24:
    months = int(input("Must be between 1 and 24 months"))

total = get_total(age, months)
print(f"Total cost: £{total:.2f}")
