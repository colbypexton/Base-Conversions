# Problem 3 
# Convert Whole Num to any base 2-16

#Essentially using the program from problem 1, but making a for loop to get each base equivalent 

def divAlgorithm(num, base):
    dict = {
    0:"0",
    1:"1",
    2:"2",
    3:"3",
    4:"4",
    5:"5",
    6:"6",
    7:"7",
    8:"8",
    9:"9",
    10:"A",
    11:"B",
    12:"C",
    13:"D",
    14:"E",
    15:"F"
}
    x=int(num)
    solution = ''
    
    while x > 0:
        q = x//base
        r = x%base
        solution = solution + dict[r]
        x = q
    finalsol = solution[::-1]
    return finalsol

count = 2
num = (input("Type your number:"))
while count < 17:
    numConverted = divAlgorithm(num, count)
    print(f"{num} = {numConverted} in base {count}")
    count += 1

