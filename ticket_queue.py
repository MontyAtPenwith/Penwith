MAX = 10
queue = []
benefits_dict = {
    #    job        discount%
    1: ("Solider",  15),
    2: ("Veteran",  20),
    3: ("Services", 10),
    4: ("Other", 5)
}

def add(name: str, benefits: str):
    if queue >= MAX:
        print("Queue is full, try again later")

    else:
        benefits = benefits.lower()
        match benefits:

            case "solider" :
                job = 1
            case 1:
                pass

            case _:
                print("Benefit job not found")
        queue.append((name, job))

