try:
    age = int(input("How old are you?"))
    country = input("where do you live?")
except ValueError:
    print("i am sorry, but that is not a valid number")
else:
    # do some sanity checks on age
    if age < 0 or age > 130: 12

        print("i am sorry, but your age cannot be negative")
    elif age > 130:
        print("i am sorry, but your age cannot be greater than 130")

    print("thank you for playing, you are", age, "years old")

try:
    age = int(input("How old are you"))
except ValueError:
    print("I am sorry, but that is not a valid number")
else:
    #Do some sanity checks on age
    if age < 0:
        print("I am sorry, but your age cannot be negative")
    elif age > 130:
        print("I am sorry, but your age cannot be negative, or greater than 130")
    if age < 18:
        print("I am sorry, but you are too young to play this game everywhere in the world.")
    elif age < 21 and country == "US":
        print ("I am sorry, but you are too young to play this game in the US.")

        print("take a shot of tequila. Thank you for playing, you are", age, "years old")

