# Problem 2 
# Convert a binary number to a Whole Num

base = 2
num = input("Enter a binary number:")[::-1]

#Checks if num is a binary number and will not go thorugh the calculation step if the num is not a binary
usableDigits = ["0", "1"]
binaryNumber = True
for digit in num:
    if digit not in usableDigits:
        print("Error: Not a Binary Number!")
        binaryNumber = False
        break

#Calculation Step

exponent = 0
total = 0
if binaryNumber == True:
    for digit in num:
        x = int(digit)
        total += x * (base**exponent)
        exponent += 1
    print(total)



