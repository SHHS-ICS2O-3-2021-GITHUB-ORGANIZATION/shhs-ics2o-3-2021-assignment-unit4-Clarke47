#NAME OF AUTHOR: Liam Clarke
#NAME OF PROGRAM: random range
#DATE OF CREATION: 23-01-22
#PURPOSE OF PROGRAM: user gives two number then I output a random one betwwen the ones givin to me
import random
# Opening text
print("Welsome ot the random number generator!")
#inputs
X = int(input("Please input your first number: "))
Y = int(input("Please input your first number: "))
#Calculating and output
x = min(X, Y)
y = max(X, Y)
random = random.randint(x, y)
print(random)