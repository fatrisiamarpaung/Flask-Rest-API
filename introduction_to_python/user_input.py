size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_metres = square_feet / 10.8

print(f"{square_feet} square feet is {square_metres : .2f} square metres.")


print("============================================================")


user_age = int(input("Enter your age: "))
months = user_age * 12
print(f"Your age, {user_age}, is equal to {months} months.")