number = int(input("Enter number: "))
print("What do you want to convert to?")

number_formats = ["Binary", "Octal", "Hexadecimal"]

for i in range(3):
    print(i+1,'.' , number_formats[i])
