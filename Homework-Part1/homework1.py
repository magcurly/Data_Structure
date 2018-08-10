b=[]
def combNumber(m, n):
    global b
    for i in range(m, n-1, -1):
        b.append(i)
        if n-1>0:
            combNumber(i-1,n-1)
        else:
            print b
        b.pop()
combNumber(5,3)