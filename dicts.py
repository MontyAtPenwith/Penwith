from ut import cmd


CATEGORIES = ("Family", "Friend", "Work", "School")

contacts = {
    "Jago":   ("9574928455", CATEGORIES[3]),
    "Oscar":  ("9899295032", CATEGORIES[1]),
    "Finley": ("0229385324", CATEGORIES[2]),
    "Thomas": ("8685903588", CATEGORIES[3]),
    "Ethan":  ("0137593256", CATEGORIES[3]),
    "Max":    ("0195203533", CATEGORIES[0])
}



running = True

def menu():
    global running

    cmd.cls()

    print("[1] -> Read phone book")
    print("[2] -> Edit phone book")
    print("[3] -> Delete contact")
    print("[4] -> Exit\n")

    choice = int(input("What do you want to do?: "))
    while choice < 0 or choice > 4:
        choice = input("Pick a valid input: ")

    cmd.cls()

    match choice:
        case 1:
            for name, (number, info) in contacts.items():
                print(f"{name} ({info}) -> {number}")

            input("")
        
        case 2:
            edit = input("Enter contact number or name: ")
            edit = edit.capitalize()
            for name, (number, info) in contacts.items():
                if name == edit or number == edit:
                    print(f"Found {edit} in contacts\n")
                    choice = input(f"Do you want to change {edit}'s number or infomation?: ")

                    searching = True
                    while searching:

                        match choice:
                            case "number" | "num" | "n":
                                searching = False
                                new_num = input(f"Enter {edit}'s new number: ")
                                old_num, category = contacts[edit]
                                contacts[edit] = (new_num, category)

                            case "infomation" | "info" | "i":
                                searching = False
                                new_info = input(f"Enter {edit}'s new number: ")
                                #########
                                num, category = contacts[edit]
                                contacts[edit] = (new_num, category)

                            case _:
                                print("\nInvalid choice")
                                choice = input(f"Do you want to change {edit}'s number or infomation?: ")

                    break
                
                else:
                    pass

            print(edit, "not found in contacts")
            input("")        

        case 3:
            pass

        case 4:
            running = False


while running:
    menu()