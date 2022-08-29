lst1=["Netflix", "Hulu", "Sling", "Hbo"]
lst2=[198, 166, 237, 125]
def create(list_1,list_2):
    return dict(zip(list_1,list_2))
print(create(lst1,lst2))