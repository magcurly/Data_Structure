def lowestcost(arr):
    if arr is False:return 0
    n=len(arr)
    m=len(arr[0])
    pre=[arr[0][0]] 
    for i in range(1,m):
        pre.append(pre[i-1]+arr[0][i])
    for i in range(1,n):
        pre[0]=arr[i][0]+pre[0]
        for j in range(1,m):
            pre[j]=min(pre[j-1],pre[j])+arr[i][j] 
    return pre[m-1] 
arr=[[1,1,1,4],[4,3,1,3],[3,1,2,1],[1,1,4,1]]
print lowestcost(arr)