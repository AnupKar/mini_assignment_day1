def convert(lis):
    final = []
    final = list(filter(lambda x: x if(x > 0) else None, map(lambda y: y*-1 , lis)))
    return final
print(convert([-1000, 500, -600, 700, 5000, -90000, -17500]))