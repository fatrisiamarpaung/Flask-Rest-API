friends = ["Rolf", "Jen", "Bob", "Anne"]

for friend in friends:
    print(f"{friend} is my friend.")


# =============================================

grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)

# --------------------------------------
grades = [35, 67, 98, 100, 100]
total = sum(grades)
amount = len(grades)


print(total / amount)