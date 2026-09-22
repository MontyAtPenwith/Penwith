import subprocess
import sys
from ut import cmd



print("1")
cmd.cls()

motion_sensor = False
armed_alarm = False
panic_button = False
panic_code = 494338
attempts = 3

choice = int(input("Enter #"))
choice2 = int(input("Enter #"))

if choice == 1 or choice2 == 1:
    motion_sensor = True
    armed_alarm = True

if choice == 3 or choice2 == 3:
    panic_button = True

if (motion_sensor and armed_alarm) or (panic_button):
    print("Burglar alarm triggered!")

    while attempts is not 0:

        code = int(input("\nEnter code to deactivate alarm: "))
        if code != panic_code:
            print("Wrong deactivation code")
            attempts -= 1
            print(f"{attempts} attempts remaining")

        elif code == panic_code:
            print("Alarm deactivated")
            sys.exit()

    print("\nPolice called!")

