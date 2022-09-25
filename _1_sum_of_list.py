def addition(no):
    total = 0
    for i in no:
        total += i
    return total
x = (8,2,3,0,7)

print("The give list for addition is :", x)
print("The sum of all the numbers in the list is : ", addition((x)))