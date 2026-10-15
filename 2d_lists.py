from ut import cmd

running = True

grades = [
    [72, 65, 80, 58],
    [90, 84, 76, 88],
    [55, 60, 48, 63]
]



def menu():

    global running
    cmd.cls()

    print("[1] -> Show student scores")
    print("[2] -> Edit student scores")
    print("[3] -> Edit a student")
    print("[4] -> Exit")

    choice = int(input("\nEnter an option to start: "))
    while choice < 1 or choice > 4 or not isinstance(choice, int):
        choice = int(input("You must enter a number between 1 and 3: "))

    match choice:
        case 1:

            cmd.cls()
            i = 1
            for student in grades:
                print(f"Student {i} total: {sum(student)} -> {student}")
                i += 1
            print("")
            input("")    

        case 2:
            cmd.cls()
            choice2 = int(input("Enter a students number: "))
            while choice2 < 1 or choice2 > len(grades) or not isinstance(choice2, int):
                choice2 = int(input(f"You must enter a number between 1 and {len(grades)}: "))

            #cmd.cls()    
            choice_student = grades[choice2 -1]
            print(f"Student {choice2} total: {sum(choice_student)} -> {choice_student}")
            print("")

            test = int(input("What number test do you want to change?: "))
            while test < 1 or test > (len(choice_student)+1) or not isinstance(choice2, int):
                test = int(input(f"You must enter a number between 1 and {len(choice_student)}: "))

                

        case 3:
            pass
        case 4:
            print("")
            running = False


while running:
    menu()