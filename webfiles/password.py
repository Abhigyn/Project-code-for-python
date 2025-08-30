
SECURE = (("s","$"),("and","&"),("a","@"),("o","*"),("i","1"),("I","|"))

def securePassword(password):
    for a,b in SECURE:
        password = password.replace(a,b)
        return password

if __name__ == "__main__":
    password = input("\nEnter Your Password")
    password = securePassword(password)
    print(f"\nYour secure password is{password}")