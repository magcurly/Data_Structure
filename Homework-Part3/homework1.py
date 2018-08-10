class Stack:
    def __init__(self):
        self.list=[]

    def IsEmpty(self):
        if len(self.list)==0:
            return True
        else:
            return False
    
    def Push(self,x):
        self.list.append(x)
    
    def Pop(self):
        if not self.IsEmpty():
            return self.list.pop(len(self.list)-1)
        else:
            return None
    
    def Top(self):
        if not self.IsEmpty():
            return self.list[len(self.list)-1]
        else:
            return None

def testlist(L,A): #T1   #spcace complexity is 1; time comlexity is N+M
    S=Stack()
    i,j=0,0
    while(True) :
        if A[j] > S.Top() or S.Top() is None :
            S.Push(L[i])
            i+=1
            #continue
        elif A[j] == S.Top():
            j+=1
            S.Pop()
        elif A[j] < S.Top():
            return False
        if j==len(A):
            return True

def testlist2(L,A): #T2
    S=Stack()
    i,j=0,0
    while j<len(A):
        if A[j] != S.Top() or S.Top() is None:
            if i==len(L):
                break
            S.Push(L[i])
            i+=1
        elif A[j]==S.Top():
            S.Pop()
            j+=1
        
    if S.IsEmpty() is True:
        return True
    else:
        return False
    

#L=['A','B','C','D','E']
#A=['C','A','D','B']
L=[0,1,2,3,4,5,6,7,8,9]
a=[4,3,2,1,0,9,8,7,6,5] #True
b=[4,6,8,7,5,3,2,9,0,1] #False
c=[2,5,6,7,4,8,9,3,1,0] #True
d=[4,3,2,1,0,5,6,7,8,9] #True
e=[1,2,3,4,5,6,9,8,7,0] #True
f=[0,4,6,5,3,8,1,7,2,9] #False
g=[1,4,7,9,8,6,5,3,0,2] #False
h=[2,1,4,3,6,5,8,7,9,0] #True
#print testlist2(L,A)
print testlist(L,a)
print testlist(L,b)
print testlist(L,c)
print testlist(L,d)
print testlist(L,e)
print testlist(L,f)
print testlist(L,g)
print testlist(L,h)