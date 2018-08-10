def powerset(nums):
    powerset = []
    res = [0] * len(nums)

    def visit(i):
        if i == len(nums):
            powerset.append([num for j, num in enumerate(nums) if res[j] == 1])
        else:
            res[i] = 0
            visit(i+1)
            res[i] = 1
            visit(i+1)

    visit(0)
    
    return powerset[1:]
li=[1,2,3]
print powerset(li)