
def enter_item(item):

    name, price = item

    name = str(name)

    while True:
        try:
            #price = float(f"{price:.2f}")
            price = float(price)

            if price <= 0:
                price = list(price)

            return name, price
        except Exception:
            print("Price must be a float")

            


while True:
    name = input("Enter your items name: ")
    price = input("Enter your items price: ")
    name, price = enter_item((name, price))

    print(name, type(name))
    print(price, type(price))