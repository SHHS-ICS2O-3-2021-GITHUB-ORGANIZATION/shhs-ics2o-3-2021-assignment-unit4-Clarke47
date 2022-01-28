#NAME OF AUTHOR: Liam Clarke
#NAME OF PROGRAM: Age checker
#DATE OF CREATION: 2022-01-22
#PURPOSE OF PROGRAM: take an age then say where they are in life

# Opening text
print("Welcome to the age checker!")
#inputs
Age = int(input("Please type your age: "))
#Calculating and output
if Age >= 5 and Age <= 11:
  print("You are in elementary school")
elif Age >= 12 and Age <= 14:
  print("You are in intermediate")
elif Age >= 15 and Age <= 18:
  print("You are in High school")
else:
  print("you are in university, college or part of the workforce")