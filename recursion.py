
def countdown(n):
    if n == 0:
        print("Lift-off")
        return 0

    print(n)
    countdown(n-1)

total = 0

def add_up(n):
    global total
    length = len(n)

    total += add_up(n-)


ls = [4, 8, 15, 16, 23, 42]
print(countdown(5))
print(add_up(ls))