PRICES = {
    "tea": 1.80,
    "coffee": 2.60,
    "scone": 3.25
}

orders = []
running = True

def add_order(item: str, quantity: int) -> None:
    orders.append((item, quantity))

def server_next() -> float:
    if len(orders) == 0:
        print("No orders are waiting")

    else:
        order = orders.pop(0)
        item = order[0]
        quantity = order[1]
        cost = PRICES[item] * quantity
        print(f"Serving {quantity} x {item}: £{cost:.2f}")
        return cost


while running:
    choice = input("Enter item name (or 'done'): ")
    choice = choice.lower()

    if choice == "done":
        total = 0
        for i in range(len(orders)):
            total += server_next()
        print(f"Total: £{total:.2f}")

        # if you want the program to run again after each order
        # comment out the line below
        running = False

    elif choice in PRICES:
        whole_number = False
        while not whole_number:
            try:
                amount = int(input(f"Enter the quantity of {choice}: "))
                while amount <= 0 or amount > 10:
                    amount = int(input("Quantity must be between 1-10: "))
                add_order(choice, amount)
                whole_number = True

            except:
                print("Amount must be a whole number")

    else:
        print("Not on the menu")
        choice = ""