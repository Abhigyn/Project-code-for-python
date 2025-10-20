# Arithmetic operations
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y
def percentage(x, y):
    return x % y
def power(x, y):
    return x ** y
def percentage(x, y):
    """Calculate y% of x."""
    return (x * y) / 100
def square(x):
    return x ** 2
def cube(x):
    return x ** 3
def square_root(x):
    if x < 0:
        return "Cannot compute the square root of a negative number!"
    return x ** 0.5
def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. percentage")
        print("6. Power")
        print("7. Unit Conversion (Centimeter to Inches / Inches to Centimeter)")
        print("8. Temperature Conversion (Celsius to Fahrenheit / Fahrenheit to Celsius)")
        print("9. Calculate Percentage")
        print("10. Square of a Number")
        print("11. Cube of a Number")
        print("12. Square Root of a Number")
        operation = input("Enter choice (1/2/3/4/5/6/7/8/9/10/11/12): ")   
        if operation not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
            print("Invalid input! Please choose a valid operation.")
            continue
        if operation in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue
            if operation == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif operation == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif operation == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif operation == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif operation == '5':
                print(f"{num1} % {num2} = {percentage(num1, num2)}")
            elif operation == '6':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")
        elif operation == '7':
            conversion_type = input("Enter 'CM' for Centimeter to Inches or 'I' for Inches to Centimeter: ").upper()
            try:
                V = float(input("Enter your number: "))
                if conversion_type == "CM":
                    I = V / 2.54
                    print(f"The conversion from Centimeter to Inches is {I}")
                elif conversion_type == "I":
                    Cm = V * 2.54
                    print(f"The conversion from Inches to Centimeters is {Cm}")
                else:
                    print("Invalid input. Please enter 'CM' or 'I'.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif operation == '8':
            conversion_type = input("Enter 'C' for Celsius to Fahrenheit or 'F' for Fahrenheit to Celsius: ").upper()
            try:
                X = float(input("Enter the temperature value: "))
                if conversion_type == 'C':
                    f = (9 * X / 5) + 32
                    print(f"The temperature in Fahrenheit is: {f}°F")
                elif conversion_type == 'F':
                    c = 5 * (X - 32) / 9
                    print(f"The temperature in Celsius is: {c}°C")
                else:
                    print("Invalid input. Please enter 'C' or 'F'.")
            except ValueError:
                print("Invalid input! Please enter a valid temperature.")
        elif operation == '9':
            try:
                num = float(input("Enter the number to calculate the percentage of: "))
                percentage_value = float(input("Enter the percentage value (1 to 100): "))
                if 1 <= percentage_value <= 100:
                    result = percentage(num, percentage_value)
                    print(f"{percentage_value}% of {num} is {result}")
                else:
                    print("Please enter a percentage between 1 and 100.")
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
        elif operation == '10':
            try:
                 n200=int(input("Enter The Number "))
                 square = lambda x:x*x 
                 print(f"{square(n200)}")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif operation == '11':
            try:
                num = float(input("Enter the number to cube: "))
                print(f"The cube of {num} is {cube(num)}")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif operation == '12':
            try:
                num = float(input("Enter the number to find the square root: "))
                print(f"The square root of {num} is {square_root(num)}")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        next_calculation = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if next_calculation != 'yes':
            print("Thank you for using the calculator!")
            break
calculator()
