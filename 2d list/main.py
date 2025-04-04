rows=int(input("how much rows do you want?"))
columns=int(input("how much columns do you want?"))
mainlist=[]

for i in range(rows):
    templist=[]
    for i in range(columns):
        answer=int(input("what would you like to add"))
        templist.append(answer)
    mainlist.append(templist)
for i in mainlist:
    print(i)
