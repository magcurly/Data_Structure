class Trituple: #define trituple
    def __init__(self,a,b,c):
        self.A=a
        self.B=b
        self.C=c
    def printtri(self):
        print [self.A,self.B,self.C]

def distance(tri): #define distance
    return abs(tri.A-tri.B)+abs(tri.A-tri.C)+abs(tri.B-tri.C)

def findmindis(A,B,C):
    map=[]
    #put every trituple in a list
    for i in A:
        for j in B:
            for x in C:
                t=Trituple(i,j,x)
                map.append(t)
    min=map[0] #initialize the first trituple as the trituple with the shortest distance
    for i in map:
        if distance(i)<distance(min):
            min=i
    min.printtri() 
    print "The minimal distance is ",distance(min)
    return
        
A = [13, 16, 19, 27]
B = [10, 14, 19, 24, 27, 35]
C = [15, 20, 23, 28, 31, 34, 38]

findmindis(A,B,C)