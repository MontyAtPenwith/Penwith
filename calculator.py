from ut import *

cmd.cls()

num_1 = float(input("Enter your first number: "))
operator = input("Input your operator (+ - * /): ")
num_2 = float(input("Enter your second number: "))

match operator:

    case "+":
        print(f"{num_1} + {num_2} = {num_1+num_2}")

    case "-":
        print(f"{num_1} - {num_2} = {num_1-num_2}")

    case "/":
        if num_1 == 0 or num_2 == 0:
            print("Cannot perform division by 0")
            cmd.exit()
        print(f"{num_1} / {num_2} = {num_1/num_2}")

    case "*" | "x" | "X":
        print(f"{num_1} X {num_2} = {(num_1*num_2)}")
 
    case _:
        print("Enter a valid operator")