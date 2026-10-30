
seated = False
plan = []
for row in range(5):
    plan.append(["-"] * 6)


def book_seat(plan: list, row: int, seat: int) -> bool:

    if plan[row][seat] == "-":
        plan[row][seat] = "X"
        return True

    else:
        return False


def count_free(plan: list) -> int:

    free = 0
    for row in range(len(plan)):
        for seat in range(len(plan[row])):
            if plan[row][seat] == "-":
                free += 1

    return free


def show_plan(plan: list) -> None:
    for i in range(len(plan)):
        print(plan[i])


while not seated:

    choice_r = int(input("Enter what row you would like to choose (0-4): "))
    while choice_r < 1 or choice_r > 4:
        choice_r = int(input("Incorrect, choose a row between 0 and 4: "))

    choice_s = int(input("Enter what seat you would like to choose (0-5): "))
    while choice_s < 1 or choice_s > 5:
        choice_s = int(input("Incorrect, choose a seat between 0 and 5: "))

    if book_seat(plan, choice_r, choice_s):
        print("Booked seat\n")
        seated = True

    else:
        print("Seat not available\n")


show_plan(plan)
