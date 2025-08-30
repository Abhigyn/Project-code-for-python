import time

def fiboIter(n):
    previousNum = 0
    currentNum = 1
    if n == 0:
        return previousNum
    elif n == 1:
        return currentNum

    for i in range(2, n + 1):
        prevPrevNum = previousNum
        previousNum = currentNum
        currentNum = previousNum + prevPrevNum
    return currentNum

# def fiboRecur(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fiboRecur(n-1) + fiboRecur(n-2)

if __name__ == "__main__":
    num = int(input("Enter a Number: "))
    
    init = time.time()
    # print(f"Using recursion, Fibonacci({num}) = {fiboRecur(num)}")
    # print(f"Recursion took {time.time() - init:.6f} seconds\n")

    init = time.time()
    print(f"Using iteration, Fibonacci({num}) = {fiboIter(num)}")
    print(f"Iteration took {time.time() - init:.6f} seconds")

