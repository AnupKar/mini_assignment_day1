lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
lst2 = list(map(lambda x: x.count("a"), lst1))
lst3 = list(map(lambda x: x.count("A"), lst1))
print(f"a: {lst2}")
print(f"A: {lst3}")