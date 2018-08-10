#def getRealSubSet(fromList,toList):
 #   if(len(fromList) <= 1):
 #  return
   # for id in range(len(fromList)):
    #    arr = [i for i in fromList if i != fromList[id]]
     #   getRealSubSet(arr,toList)
        #print arr
      #  if(toList.count(arr) == 0):
       #     toList.append(arr)
#li = []
#getRealSubSet([1,2,3,4],li)
#li.sort()
#print li

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