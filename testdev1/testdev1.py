def gh(x,y,z):
    a=[]
    if x not in a:
        a.append(x)
    elif y not in a:
        a.append(y)
    elif z not in a:
        a.append(z)
    return a
print(gh({1:3,33:5,12:4,2:5,6:7},{1:4,33:5,12:4,5:5,6:7},{1:3,3:5,12:4,2:5,9:7}))
