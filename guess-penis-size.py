#!/usr/bin/env python3

import random
import decimal
import time

rand = float(decimal.Decimal(random.randrange(75,200)))/100

print("This program will approximate your true penis size with data you input.")
time.sleep(2)

while True:
    play = input("Are you ready to play? ").lower()
    if play == "no":
        print("Fine, you probably have a small penis anyway.")
        quit()

    else:
        print("Okay then.. let's measure that penis!")
        break
time.sleep(2)

input("What is your height in feet? (Use decimal for inches.) ")
score1 = rand

input("What is your weight in pounds? ")
score2 = rand

input("Are you of African ethnicity? ")
score3 = rand

input("Are you related to J^raxis? Note: If so, you have small penis genes. ")
score4 = rand

input("What size is your foot using U.S. measurement? ")
score5 = rand

input("Do you eat a lot of fruit and vegetables? ")
score6 = rand

input("Are you circumsized? ")
score7 = rand

final_size = score1 + score2 + score3 + score4 + score5 + score6 + score7
print("Your penis size is: ", final_size, "inches!")
