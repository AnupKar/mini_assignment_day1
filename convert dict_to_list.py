dict={"HueX":[1,2,3],"is":[7,6],"best":[4,5]}
dictItem=dict.items()
k=list(dict.keys())
v=list(dict.values())
finalList=[]
print(f"dictItem: {dictItem}, k: {k}, v: {v}")
for i in range(3):
    lis1=[]
    lis1.append(k[i])
    if type(v[i]) is list:
        for j in v[i]:
            lis1.append(j)
    print(lis1)
    finalList.append(lis1)
print(finalList)
