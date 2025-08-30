import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowersal
    e
    # print(s1)
    s2 = string.ascii_uppercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)
    plen = int(input("Enter Password length\n"))
    s =[]
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    # random.shuffle(s)
    print("Your Password is\n")
    print("".join(random.sample(s,plen)))