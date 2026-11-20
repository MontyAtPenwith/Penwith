import statistics

class_a: list = [56, 78, 91, 100, 42, 78, 85]
class_b: list = [67, 100, 73, 59, 100, 88, 91]

def analyse(scores: list[int]) -> tuple:
    if len(scores) == 0:
        return None
    
    #       highest      lowest       mean (rounded)
    return (max(scores), min(scores), round(statistics.mean(scores), 1))

hi, low, avg = analyse(class_a)
print("Class A test scores:")
print(f"Minimum - {low}")
print(f"Maximum - {hi}")
print(f"Average - {avg}\n")

hi, low, avg = analyse(class_b)
print("Class B test scores:")
print(f"Minimum - {low}")
print(f"Maximum - {hi}")
print(f"Average - {avg}")

