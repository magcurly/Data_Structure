def MaxSub_sum(A):
    sum=0
    maxSum=A[0]
    for i in range(len(A)):
        sum += A[i]
        if sum > maxSum:
            maxSum = sum
        elif sum <0:
            sum = 0
    return maxSum
#A=[2, 4, -7, -5, -3, -2, -7, -6, -9, -10, -2]
A=[-2, 11, -4, 13, -5, -2]
B=[-6, 2, 4, -7, 5, 3, 2, -1, 6, -9, 10, -2]
print MaxSub_sum(A)
print MaxSub_sum(B)