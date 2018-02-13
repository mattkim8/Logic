def Div(n):
    l = []
    if n > 0:
        for i in range(1,n+1):
            if n%i == 0:
                l.append(i)
                l.append(-i)
    else:
        for i in range(n,0):
            if n%i==0:
                l.append(i)
                l.append(-i)
    return l

#4b
def count(n):
    for i in range(n):
        if len(Div(i)) > 60:
            print i, Div(i)


#4c          
def count2(n):
    l = []
    for i in range(n):
        if len(Div(i)) % 2 != 0:
            l.append(i)
    return l


def Euc(n,m):
    if m == 1:
        return n
    return Euc(m,n%m)



