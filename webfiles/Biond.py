import os
nbinod= 0
def isbiond(filename):
    with open(filename,"r") as f:
        fileContent =f.read()
        if "binod" in fileContent.lower():
            return True
        else:
            return False
    if __name__ == "__main__":
        dir_contents = os.listdir()
        print(f"{dir_contents}:\n")
        for item in dir_contents:
            if item.endswith(".txt"):
                print(f"Detecting Binod in {item}:\n")
                flag = isbiond(item)
                if (flag):
                    print(f"Binod found in {item}:\n")
                    nbinod += 1
                else:
                    print(f"Binod not found in {item}:\n")
print("Binod Detectr sumary")
print(f"{nbinod} files found  with Binod hidden into them")