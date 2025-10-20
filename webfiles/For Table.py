def multiply(z1):
    for i in range(1,11):
        Table=(str(f"{z1} X {i}= {z1*i}"))
        "/n".join(Table)
        print(Table)
K1=int(input("Enter Number "))
multiply(K1)