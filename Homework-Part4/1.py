
def movepattern(arr):
    n=len(arr)
    m=len(arr[0])
    #无论多少种走法，到了终点可以算到走法的总数
    map=[[1]] #将初始点的路线矩阵作为1

    for i in range(n):
        for j in range(m):
            map[i].append(0) #当某点还没走，设为0
            if arr[i][j]==1: #若遇到阻碍，则该点无法前进，将路线矩阵中该点设为0
                map[i][j]=0
                continue
            if i>=1 and j >=0 and arr[i-1][j]==0: #若该点可以通行
                map[i][j]+=map[i-1][j] #向下行走
            if j>=1 and i>=0 and arr[i][j-1]==0:
                map[i][j]+=map[i][j-1] #向右行走
        map.append([])
    return map[n-1][m-1] #终点路线矩阵值为实际可行走的路线数

arr=[[0,0,0,0,0],[0,1,0,1,0],[0,0,0,0,0]]
print movepattern(arr)
