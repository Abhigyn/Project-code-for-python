a = int(input("Enter The Number\n"))
b = int(input("Enter The Number\n"))
if a>b:
    mn=b
else:
    mn=a
for i in range(1,mn+1):
    if(a%i == 0 and  b%i == 0):
        HCF= i
print(f"The HCF/GCC of {a} and {b} is {HCF}\n")