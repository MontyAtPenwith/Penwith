

def draw_rect(height: int, width: int, symbol="*") -> None:

    print(symbol*width)
    for h in range((height-2)):
        print(symbol, " "*(width-4), symbol)
    print(symbol*width)


def greet(name: str, time: str) -> None:
    print(f"Hello {name}")
    print(f"The time is {time}")

draw_rect(10,10)
greet("Monty", "16:04")

print("x" * 20)