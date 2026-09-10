

print("< 1 > - Binary")
print("< 2 > - Denary")
print("< 3 > - Hex")
choice = int(input("\nEnter your option: "))

if choice == 1:
    bin = input("Enter your binary number: ")
    h_bin = hex(bin)
    d_bin = int(bin)
    print(f"\nDen -> {d_den}")
    print(f"Hex -> {h_den.upper()[2:]}")
    
elif choice == 2:
    den = int(input("Enter your denary number: "))
    b_den = bin(den)
    h_den = hex(den)
    print(f"\nBin -> {b_den[2:]}")
    print(f"Hex -> {h_den.upper()[2:]}")
    
elif choice == 3: 
    hex = input("Enter your hex number: ")
    hex = hex.upper()
    b_hex = bin(int(hex, 16))
    d_hex = int(hex, 16)
    print(f"\nDen -> {d_hex}")
    print(f"Bin -> {b_hex[2:]}")
    
elif isinstance(choice, float):
    print("Enter a whole number!")
    
    
else:
    print("error")

