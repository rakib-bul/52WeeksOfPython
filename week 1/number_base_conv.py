number = int(input("Enter number: "))
print("What do you want to convert to?")

number_formats = ["Binary", "Octal", "Hexadecimal"]

for i in range(3):
    print(i+1,'.' , number_formats[i])
try:
    choice = int(input("Enter choice: "))
    if choice == 1:
        print(f"Binary: {bin(number)[2:]}")
    elif choice == 2:
        print(f"Octal: {oct(number)[2:]}")
    elif choice == 3:
        print(f"Hexadecimal: {hex(number)[2:]}")
    else:
        print("Invalid choice")

except ValueError:
    print("Enter a valid number")