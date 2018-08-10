def  MinD(A, x, y) :
    n = len(A)
    Min, d1, d2 = 1000, -1, -1
    for i in range(n) :
        for  j in range(i, n) :
            if  A[i] == x and A[j] == y or A[i] == y and A[j] == x : 
                if  abs(i-j) < Min : 
                    Min, d1, d2 = abs(i - j), i, j
    return Min, d1, d2

def mindistance(A, x, y):
    min = len(A)
    point = 0
    for i in range(len(A)):
        if A[i] == x or A[i] == y:
            if A[point]!=x and A[point]!=y:
                point=i
            else:
                if A[point] != A[i]:
                    if min > abs(point-i):
                        min = abs(point-i)
                point=i
    return min

A = [1,2,6,5,6,7,4,3,2,3,1,5,9,8,6,4,2,5]
print mindistance(A,5,1)