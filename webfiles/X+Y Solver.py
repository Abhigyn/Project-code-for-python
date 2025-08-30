import time

def transformed(b):
    for i in range(len(b)-1):
        if b[i] == "1":
            b[i] = "0"
            if b[i + 1] == '0':
                b[i + 1] = "1"
            else:
                b[i + 1] = "1"
    return b
if __name__ == "__main__":
    a = list("123456789")
    c = time.time() 
    print(f"{time.time() - c:.9f}")
    print(a)
    while a != transformed(a.copy()):
        a = transformed(a.copy())
d = time.time()
print(f"{time.time() - d:.9f}")
print(a)