
running: bool = True

while running:
    complete: bool = True
    choice: str = ""
    choice = input("Please enter a password: ")

    if (len(choice) <= 7 or len(choice) >= 21):
        print("Must be 8 - 20 characters")
        complete = False

    if not any(i.isalpha() for i in choice):
        print("Must contain a letter")
        complete = False

    if not any(i.isdigit() for i in choice):
        print("Must contain a digit")
        complete = False

    print("\n")

    if complete: 
        running = False


print(f"Password accepted: {choice[0]}{'*' * (len(choice) - 2)}{choice[-1]}")
