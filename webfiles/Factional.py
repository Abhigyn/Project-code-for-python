


def Factorial(number):
    if number == 0 or number == 1 :
        return 1
    else:
        return number * Factorial(number - 1)


def FactorialTrailingZeros(number):
    fac = Factorial(number)
    print(fac)
    count = 0
    while (fac%10 == 0):
        count = count +1
        fac = fac/10
        return count



if __name__ == "__main__":
    number = int(input("Enter a number\n"))
    # Fac = Factorial(number)
    # print(f"The Factorial Number is {Fac}")
    print(FactorialTrailingZeros(number))