def dset(li):
    arr=[]
    b=[]
    def pick(li,m):   
        for i in range(len(li)-1,m-2,-1):
            b.append(li[i])
            ls=li[0:i]
            if m-1>0:
               pick(ls,m-1)
            else:
               #print sorted(b)
               arr.append([num for j,num in enumerate(sorted(b))])
            b.pop()
    for id in range(3,0,-1):
        pick(li,id)
    return sorted(arr)
group=[1,2,3]
print dset(group)