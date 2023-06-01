#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of %i is " %number, end="")
if number < 0:
    number *= -1
if number % 10 > 5:
    print("%i and is greater than 5" %(number % 10))
elif number % 10 == 0:
    print("%i and is 0" %(number % 10))
else:
    print("%i and is less than 6 and not 0" %(number % 10))
