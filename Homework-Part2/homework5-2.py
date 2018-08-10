
def main(List):
	B=0
	for i in List:
		if B==0:
			A=i
			B=1
		elif i == A:
			B+=1
		elif i != A:
			B-=1
	
	if B>1:
		return A
	else:
		return -1

List=[1,2,3,1,2,3,2,3,2,1,2,1,1,2,2,2]
print main(List)
		
