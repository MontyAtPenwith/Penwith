from random import randint
from ut import cmd

running = True
i = 1
num = randint(1, 50)
cmd.cls()


a = cmd.accept_num("Enter")
print(a)

while running:
    n = True

    while n:
        try:
            choice = int(input("Enter a number between 1-50: "))
            n = False
        except Exception:
            print("Enter a valid number between 1-50")

    if choice == num:
        print(f"Correct in {i} attempts")
        cont = input("Do you want to play again: ")
        if cont.lower() in ["y", "ye", "yes", "ya"]:
            cmd.cls()
            num = randint(1, 50)
            i = 1

        else:
            running = False

    elif choice > num:
        i += 1
        n = True
        print("Too big")

    elif choice < num:
        i += 1
        n = True
        print("Too small")

    else:
        print("fff")