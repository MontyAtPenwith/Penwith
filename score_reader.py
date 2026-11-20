import statistics

all_scores: list[int] = []

try:
    with open(r"jn\scores.txt", "r") as file:
        content: str = file.readlines()

except FileNotFoundError:
    print("File doesn't exist")


print("Name    - Score")
print("")

for line in content:

    line = line.strip().split(",")

    name: str = line[0]
    scores: int = line[1]

    
    print(f"{name:<7} - {scores:>5}")

    all_scores.append(int(scores))

print("")
print(f"Highest - {max(all_scores):>5}")
print(f"Lowest  - {min(all_scores):>5}")
print(f"Average - {round(statistics.mean(all_scores), 1):>5}")


print("")