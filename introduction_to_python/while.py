from ast import While


number = 7

while True:
    user_input = input("Would like to play? (Y/n) ")

    if user_input == "n":
        break

    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You Guessed correctly!")
    elif abs(number - user_number)== 1:
        print("You were off by one")
    else:
        print("Sorry, it's wrong!")

    # elif number - user_number in (1, -1): -. other way