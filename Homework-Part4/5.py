def submat(arr):
    n=len(arr)
    f=[[]]
    #第0行为哨兵行
    for i in range(1,n+1):
        f.append([])
        f[i].append(0)#第0列为哨兵列
        f[i].append(arr[i-1][0])#存入第1列
    for i in range(1,n+1):
        for j in range(2,n+1):
            f[i].append(f[i][j-1]+arr[i-1][j-1]) #将第i行第j列元素之前的所有元素（包括第j个元素）加和起来
    
    p=[None] #p[k]为固定第i到j列求得包括从第1到k行范围内的最大子矩阵和
    q=[None] #q[k]为固定第i到j列，从第1行道第k行的最大子矩阵
    max=None #任何值大于None
    #以下算法时间复杂度为O(n^3)
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            p.append(f[1][j]-f[1][i-1]) #p[k]为固定i和j求得包括k行的最大子矩阵和
            x,y=1,1 #行的上下界从1开始
            q.append(p[1])
            for k in range(2,n+1):
                if p[k-1]>0:
                    p.append(p[k-1]+f[k][j]-f[k][i-1])
                else:
                    p.append(f[k][j]-f[k][i-1])
                    x=k #获得行上界
                y+=1 #获得行下界
                if q[k-1]>p[k]:
                    q.append(q[k-1])
                    
                else:
                    q.append(p[k])
            if q[n]> max:
                max=q[n] #第i到j列范围内最大的和
                ii=i-1
                ij=j-1
                ix=x-1
                iy=y-1
    answer=[]
    for i in range(ix,iy+1):
        answer.append(arr[i][ii:ij+1])
    return answer,max

arr=[[0,-2,-7,0],[9,2,-6,2],[-4,1,-4,1],[-1,8,0,-2]]
print submat(arr)