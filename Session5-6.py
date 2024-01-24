name = input("what is your name?")
age = input("how old are you?")
age = int(age)
birth_year= 2023 - age
print (f"OMG {name}, you are {age} years old so you were born in {birth_year}!")
print ("OMG", name, ", you are", age, "years old so you were born in", birth_year)

try:
    age1 = int(input("what is your age player 1?"))
    age2 = int(input("what is your age player 2?"))
    res = age1/age2
except ValueError
    print("i am sorry , but that is not a valid number")
except ZeroDivisionError
    print("i am sorry , but you cannot divide by zero")
except:
    print("i am sorry, but something went wrong")
else:
    print("player 1 is older than player 2 by a factor of", res)
finally:
    print("thank you for playing")
    

