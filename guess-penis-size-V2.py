#!/usr/bin/env python3

# v2.0 updated using a function to calculate a graduating score
# messing around with modules, variables, functions, if/else loop
# author: hazeyez

"""
using bash, run the script 1000x & save output to a file to get dataset to test best average of range

bash$ "for i in {1..1000}; do python3 guess-penis-size-V2.py >> output.txt; done"

ranges tested x1000 iterations each:

80,150 = average 6.86 inches
80,200 = average 8.36 inches
80,250 = average 9.86 inches
80,300 = average 11.34 inches

as you can see, every +50 the range is increased, the average consistently increases ~1.5 inches
"""

import random
import decimal
import time

zero = 0

def rando(base_score):
    score = base_score + float(decimal.Decimal(random.randrange(80,200)))/100
    return score


play = input("Are you ready to play? [yes/no] ").lower()
if play == "no":
    print("Fine, you probably have a small penis anyway.")
    quit()

else:
    print("Okay then.. let's measure that penis!")
  
time.sleep(2)

input("What is your height? ")
score = rando(zero)

input("What is your weight? ")
score += rando(zero)

input("Are you of African ethnicity? ")
score += rando(zero)

input("Are you related to J^raxis? Note: If so, you have small penis genes. ")
score += rando(zero)

input("What size is your foot using U.S. measurement? ")
score += rando(zero)

input("Do you eat a lot of fruit and vegetables? ")
score += rando(zero)

input("Are you circumsized? ")
score += rando(zero)
time.sleep(2)

print("Your penis size is: ", score, "inches!")
