def findcentre(A):
  max=0
  B=[]
  for i in range(len(A)):
    if A[i]>max:
      max=A[i]
      if A[i+1]<max:
        i+=1
        continue
      else:
        B.append(A[i])
  return B
         
A=[3,1,6,5,4,7,9,8,10,14,12]
print findcentre(A)
                        