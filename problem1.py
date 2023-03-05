# Problem 1
# Convert Whole Num to Base 2 (Binary)



#Went ahead and created a function that can convert a whole number to any base not exceeding 16
#The function is called divAlgorithm() which takes in two arguments: the whole number and the base
#However, for the first program the base is set to only 2 so we will let base = 2 


#Program 1
num = (input("Type your number:"))
base = 2

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

print(divAlgorithm(num, base))

