
# get number from user
num = int(input("Enter your whole number: "))

# change number into hex and binary respectively
hex_num = hex(num)
bin_num = bin(num)

# print out all
print(f"Hex:    {hex_num}       -> {hex_num[2:]}")
print(f"Binary: {bin_num} -> {bin_num[2:]}")
