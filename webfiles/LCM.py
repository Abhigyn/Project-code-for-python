a = int(input("Enter The Number\n"))
b = int(input("Enter The Number\n"))
MaxNum= max(a, b)
while(True):
    if (MaxNum%a == 0 and MaxNum%b == 0):
        break
    MaxNum = MaxNum + 1
print(f"The LCM of {a} and {b} is {MaxNum}\n")