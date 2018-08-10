def  MaxDiff( A ) : 
    n = len(A) 
    dmax = 0
    for  i in range(n) :
        for  j in range(n):
            if  i < j and A[i] - A[j] > dmax :
                dmax = A[i] - A[j]
    return dmax 

def MaXD(A):
    max=A[0]
    min=A[0]
    for i in range(len(A)):
        if A[i]>max:
            max=A[i]
        if A[i]<min:
            min=A[i]
    
    return max-min

A=[3,6,2,-30,8]
print MaXD(A)