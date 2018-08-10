def testsymmetry(st):
    if len(st) <=1:
        return 0
    q=l=len(st)
    
    for p in range(l):
        s=st[p:q]
        if len(s)<=1:
            break
        elif s==s[::-1]:
            return len(s)
        elif p!=q:
            q-=1
        elif p==q:
            q=l
            p+=1
        
    return 0
            
def manacher(s):
    if len(s)<=1:
        return 0
    t='?'
    T=[t]
    for c in s:
        T.append(c)
        T.append(t)
    c,r,size = 1,2,len(T)
    P=[0,1]+[None]*(size-2)
    maxIndex,maxCount=0,1
    for i in range(2,size):
        m=c*2-i
        if r>i and P[m]<r-i:
            P[i]=P[m]
            continue
        count=min(i,size-i-1)
        for n in range((1 if r <= i else r+1-i),count+1):
            if T[i+n]!=T[i-n]:
                count=n-1
                break
        c=i
        r=i+count
        P[i]=count
        if count >maxCount:
            maxCount=count
            maxIndex=i-count
    maxIndex=maxIndex //2
    return maxCount


s='google'

print manacher(s)
#print testsymmetry(s)