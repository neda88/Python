import random

Upperbound = int(input("Please enter a positive integer number for Upper Bound : "))
Lowerbound = int(input("Please enter a positive integer number for Lower Bound : "))
while Lowerbound >= Upperbound:
    print("Invalid Answer!")
    Lowerbound = int(input("Please enter a positive integer number for Lower Bound : "))
number = random.randint(Lowerbound, Upperbound)
guess = int(input("Please guess number between Upper Bound and Lower Bound : "))
count = 1
while guess != number:
    count += 1 
    if guess< number:
        guess = int(input("Guess Larger: "))
    elif guess > number:
        guess =int(input("Guess Smaller: "))
print("Congradulations, you guessed it right in {} times".format(count) )
