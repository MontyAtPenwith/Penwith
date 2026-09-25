total = 0
prices = [4.50, 12.99, 3.20, 7.85, 1.00, 9.99]
count = 0

for price in prices:
    if price > 5:
        count += 1

    total = total + price

print(f"Count: {count}")
print(f"Total: {total}")
