import subprocess

orders = []
available = True

while True:
    not_int = True
    choice = 0

    subprocess.call('cls', shell=True)
    print("1 -> Take a new order")
    print("2 -> Serve a customer")
    print("3 -> Open drive through")
    print("4 -> Close drive through")

    if available:

        if len(orders) < 1:
            print("\nNo cars are waiting")
        else: 
            print("\nOrders:")
            for i in range(len(orders)):
                print(f"{i+1}. {orders[i]}")


    else:
        print("\nDrive through is closed")

    while not_int:
        try:
            choice = int(input("\nPick an option: "))
            not_int = False
        except:
            print("Enter an integer")


    match choice:
        case 1:
            order = input("\nWhat is the order?: ")
            orders.append(order)

        case 2:
            if orders:
                order = orders.pop(0)
                print(f"\nThe order '{order}' was completed")
                input()

            else:
                print("\nNo orders available")
                input()

        case 3:
            if available:
                print("\nDrive through is already open")
                input()
            else:
                print("\nOpening drive through")
                available = True
                input()

        case 4:
            if not available:
                print("\nDrive through is already closed")
                input()
            else:
                print("\nClosing drive through")
                available = False
                orders = []
                input()
