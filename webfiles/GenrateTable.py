def GenerateTable(n):
    table = ""
    for i in range(1, 11):  
        table += f"{n} X {i} = {n*i}\n"  
    with open(f"I:/Study/Golu lession/C lanuge/Table/table_{n}.txt", "w") as f:
        f.write(table)
for i in range(1, 11):
    GenerateTable(i)