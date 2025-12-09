import random

def guess_num():
    number = random.randint(0,10)
    user_input = int(input("Guess the number from 0 to 10: "))

    while user_input != number:
        if user_input > number:
            user_input = int(input("Try smaller number: "))
        else:
            user_input = int(input("Try higher number: "))
    
    print("You`re right")
    

guess_num()
