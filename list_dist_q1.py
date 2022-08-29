def flat(input):
    flatList = []
    for element in input:
        if type(element) is list:
            frequency={}
            for i in element:
                if i in frequency:
                    frequency[i]+=1
                else:
                    frequency[i]=1
            for key,value in frequency.items():
                if value>1:
                    print(key, '->', value)
        else:
            pass
    return flatList
 
input = [[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]
flat(input)