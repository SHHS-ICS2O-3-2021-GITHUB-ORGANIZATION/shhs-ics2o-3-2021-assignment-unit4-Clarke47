#NAME OF AUTHOR: Liam Clarke
#NAME OF PROGRAM: Guessing Game
#DATE OF CREATION: 2022-01-21
#PURPOSE OF PROGRAM: Input a range of numbers then a random one is selected which you hvce to guess, then will displ;ay the ammount of guesses

import random
# Variables
Guesses = 1
g = 12
# Opening text
print("Welcome to random number generator") 
#Inputs for high and low numbers
low = int(input("Please input the lowest number you want: "))
high = int(input("Please input the highest number you want: "))
#Calculating and output
Answer = random.randint(int(low),int(high))#selecting random number from inputs
print("Alright you can start guessing")
while Answer != g: #makling a loop
  Guess = int(input("Whats your guess?: ")) # input for the guesses
  if Guess == Answer: # what to do if guess is right
    print(f"\n\n\n\n\nYou guessed it! It took {Guesses} tries!")
    exit()
  elif Guess != Answer:  # what to do if guess is wrong
    if Guess >= low and Guess <= high: #says if your wrong but in the range
      print("Try again :( \n\n")
      Guesses = Guesses + 1
    else: # what to do if they chose a number out of the range
      print(f"Dude, it's between {low} and {high}\n\n")