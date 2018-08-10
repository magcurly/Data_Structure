
def find(List):
	C,D=0,0
	for i in range(len(List)):
		if C==0:
			A=List[i]
			C=1
		elif D==0 and A != List[i]:
			B=List[i]
			D=1
		elif A==List[i]:
			C+=1
		elif B==List[i]:
			D+=1
		elif A!=List[i] and B!=List[i]:
			C-=1
			D-=1
	if C>1 and D>1:
		return A,B
	elif C>1 and D<=1:
		return A
	elif D>1 and C<=1:
		return B
	else:
		return -1

L1=[1,2,3,2,1,2,3,3,3,2]
L2=[1,2,3,1,2,3,1,2,3]
print find(L1)
print find(L2)
