#NAME OF AUTHOR: Liam Clarke
#NAME OF PROGRAM: Carpet cost
#DATE OF CREATION: 22-01-22
#PURPOSE OF PROGRAM: calculate cost of a carpet

# Opening text
print("This is the carpet price calculator!")
#inputs
width = float(input("Please type in your width: "))
length = float(input("Please type in your length: "))
# Calculating and output
print(f"The cost of your carpet will be {2.25 * (width * length)}")