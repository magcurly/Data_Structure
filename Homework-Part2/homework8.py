def dis(x,y,z):
      return abs(x-y)+abs(y-z)+abs(x-z)


def mindis(A,B,C):
    i,j,k=0,0,0
    min=dis(A[0],B[0],C[0])
    L=[A[0],B[0],C[0]]
    while i<len(A) and j<len(B) and k<len(C):
        dist=dis(A[i],B[j],C[k])
        if dist<min:
            min=dist
            L=[A[i],B[j],C[k]]
        if A[i]<B[j]:
            if A[i]<C[k]:
                i+=1
            else:
                k+=1
        else:
            if B[j]<C[k]:
                j+=1
            else:
                k+=1
    print "The minimal distance is",min
    return L
  
A=[0,1,2]
B=[1,2,3]
C=[2,3,4]
print mindis(A,B,C)