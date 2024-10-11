name = input("What is your name: ")
weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")

print("Hey there! " + name)
if unit.upper() == "L":
    convert = weight * 0.45
    print(f"Your weight is  {convert} kilograms.")
else:
    convert = weight/0.45
    print(f"Your weight is  {convert} pounds.")

