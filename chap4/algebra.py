def equation(a,b,c,d):
    '''solves equations of the
    form ax + b = cx + d'''
    return (d - b)/(a - c)

ret = equation(12,18,-34,67)
print(ret)