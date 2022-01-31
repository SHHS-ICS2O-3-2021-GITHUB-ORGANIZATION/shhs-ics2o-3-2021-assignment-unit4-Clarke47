#NAME OF AUTHOR: Liam Clarke
#NAME OF PROGRAM: math questions
#DATE OF CREATION: 2022-01-21
#PURPOSE OF PROGRAM: make addition and multyplication questions

import random
# Variables
x = random.randint(1, 2)
h = 100
f = "+"
high = random.randint(1, h)
low = random.randint(1, h)
# Opening text
print("Welcome to math questions") 
#Calculating and output
if x == 1:
  h = 12
  f = "*"
print(f"What is {high} {f} {low}?")