#!/usr/bin/env python3

import random
import decimal

zero = 0

def rando(base_score):
    score = base_score + float(decimal.Decimal(random.randrange(80,150)))/100
    return score

input("Yes/No?")
score = rando(zero)
#print(score)

score += rando(zero)
#print(score)
score += rando(zero)
#print(score)
score += rando(zero)
#print(score)
score += rando(zero)
#print(score)
score += rando(zero)
print(score)
