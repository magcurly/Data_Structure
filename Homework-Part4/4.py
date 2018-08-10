def roadlength(arr):
    n=len(arr)
    data=[arr[n-1]] #从树塔底层开始计算

    for i in range(n-2,-1,-1):
        sum=[] #将第i层的每点最大值存入sum列表
        k=len(data[0])
        for j in range(0,k-1):
            tmp=max(data[0][j],data[0][j+1])
            sum.append(tmp+arr[i][j])
        data.insert(0,sum)
    return data[0][0] #树塔顶层即为所求最大路径长度

#以多维数组存储树塔
arr=[[17],[13,31],[11,20,15],[25,23,35,19],[14,22,37,18,14]]
print roadlength(arr)