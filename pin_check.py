from ut import cmd

TXT = r"C:\Users\mc494338\OneDrive - Truro and Penwith College\Desktop\1\jn\pins.txt"
ATTEMPTS = 4

def load() -> str:

    try:
        # open with read 
        with open(TXT, "r") as file:
            contents = file.read()
            return contents

    except:
        print(f"Error loading {TXT}")


def save(username: str, password: int) -> bool:

    token = f"{username}:{password}"

    # open with read append
    with open(TXT, "a+") as file:
        for line in file:
            if line == token:
                print("Username and password already exists in database")
                return False

            else:
                file.write(f"\n{token}")
                return True


def check(username: str) -> bool:

    # open with read append
    with open(TXT, "r") as file:
        for line in file:
            if line == "\n":
                continue

            line = line.split(":")
            if line[0] == username.lower():
                print("User found")
                return True

            else:
                print("User not found")
                return False

def main():

    print("1. Make account")
    print("2. Login to account")
    print("3. Delete account")
    choice = int(input("Enter option #"))

    if choice == 1:
        username = input("Enter your username")
        password = input("Enter your password")

        #if save(username, password):
            


main()