#NAME OF AUTHOR: Liam Clarke
#NAME OF PROGRAM: math quick
#DATE OF CREATION: 23-01-22
#PURPOSE OF PROGRAM: outputs random addition question
import random
g = 10
p = 0
x = random.randint(1, 100)
y = random.randint(1, 100)
#Calculating and output
while g == 10:
  if p == 0:
    print(f"What is {x} + {y}?")
  answer = int(input())
  if answer == x+y:
    print("You got it!")
    exit()
  elif answer != x+y:
    print("try again >:(")
  p = p +1