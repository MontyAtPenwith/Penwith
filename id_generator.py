
full_name = "Ada lovelace"
staff_code = "48213"

def split_name(fullname: str) -> tuple:

    first = "empty"
    last = "empty"

    if not (fullname.isalpha() or "-" in fullname or " " in fullname):
        print("Name must be only letters and -'s")
        return
    
    name = fullname.split(" ")

    if len(name) >= 2:
        first = name[0]
        last = name[-1]
    elif len(name) <= 1:
        print("Please enter your full name next time")
        return
    else:
        print("split name error")

    first = first[0].upper() + first[1:]
    last = last[0].upper() + last[1:]
    initials = first[0] + last[0]
    
    return (first, last, initials)

def check_code(code: str) -> str:

    if not code.isdigit():
        print("Staff code must be digit only")
        return get_id()
    else:
        return code


def get_name() -> str:

    name_choice = input("Enter in your fullname: ")
    if not name_choice:
        print("Using backup name")
        name_choice = full_name

    return name_choice

def get_id() -> str:

    code_choice = input("Enter your ID number: ")

    if not code_choice:
        print("Using backup code")
        code_choice = staff_code

    return code_choice


try:
    name = get_name()
    first, last, initials = split_name(name)
    id = get_id()
    id = check_code(id)
except:
    print("Restart\n")
    import sys, subprocess
    subprocess.call([sys.executable] + sys.argv)
    sys.exit()
    
    

print(first, last, initials, id)