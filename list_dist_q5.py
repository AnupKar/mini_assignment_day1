from heapq import merge


dict1={"Ten":10,"Twenty":20,"Thirty":30}
dict2={"Thirty":30,"Forty":40,"Fifty":50}
def mergeDict(dict1,dict2):
    z=dict1.copy()
    z.update(dict2)
    return z
print(mergeDict(dict1,dict2))