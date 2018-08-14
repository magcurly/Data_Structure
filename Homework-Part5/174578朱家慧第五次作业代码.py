class BinTreeNode: 
    def __init__(self,dat):
        self.data=dat
        self.left=None
        self.right=None
    def GetData(self):
        return self.data
    def SetData(self,item):
        self.data=item
    def SetLeft(self, L):
        self.left=L
    def SetRight(self,R):
        self.right=R

class BinTrLList:       ##继承          ##多态，不同类都可以拥有同一函数，都可以调用。
                                        ##所有面向对象方式编写的python程序都是模块，可以进行重复使用
    def __init__(self,A=[]): 
        L=len(A)
        if L==0:
            self._root=None
        else:
            if L>0:
                B=[0 for i in range(L)]
                for i in range(L):
                    if A[i]!=0:
                        B[i]=BinTreeNode(A[i])
                for i in range(L):
                    if 2*i+1<L and A[i]!=0 and A[2*i+1]!=0:
                        B[i].left=B[2*i+1]
                    if 2*i+1<L and A[i]!=0 and A[2*i+2]!=0:
                        B[i].right=B[2*i+2]
                self._root=B[0]
    def IsEmpty(self):
        if self._root==None:
            return True
        else:
            return False
    def root(self):
        return self._root
    def lchild(self):
        return self._root.left
    def rchild(self):
        return self._root.right
    def set_root(self,rootnode):
        self._root=rootnode
    def set_left(self,leftchild):
        self._root.leftchild
    def set_right(self,rightchild):
        self._root(self,rightnode)
    
def IsBalaced(BinTree): #T1
    def Depth(t): 
        if t==None: return 0
        else: return 1+max(Depth(t.left),Depth(t.right))

    if BinTree.IsEmpty():
        return 0
    
    rheight=Depth(BinTree._root.right)
    lheight=Depth(BinTree._root.left)
    return abs(rheight-lheight)<=1 

def POrder(T): #T2
    if T.IsEmpty(): return
    p=T._root
    q=[p]
    l=[]
    cs,ps=0,1 #
    i=0
    while True:
        if i%2==0:
            p=q.pop()
            if p.left is not None:
                q.insert(0,p.left)
                cs+=1
            if p.right is not None:
                q.insert(0,p.right)
                cs+=1
        if i%2!=0:
            p=q.pop(0)
            if p.right is not None:
                q.append(p.right)
                cs+=1
            if p.left is not None:
                q.append(p.left)
                cs+=1
        l.append(p.data)
        ps-=1
        if ps==0:
            i+=1
            ps=cs
            cs=0
        if q:
            continue
        else: break
    return l

def roadco(T,N): ##T3
    if T.IsEmpty(): return
    t=T._root
    def roadcost(t,N):
        if t.data==N:
            print t.data
        else:
            if t.left !=None:
                roadcost(t.left,N-t.data)
            if t.right!=None:
                roadcost(t.right,N-t.data)
        
    roadcost(t,N)

def treediameter(T): ##T4
    if T.IsEmpty():return 0
    p=T._root
    def Depth(t):
        if t==None: return 0
        else: return 1+max(Depth(t.left),Depth(t.right))

    def diameter(t):
        if t==None: return 0
        else:
            ld=diameter(t.left)
            rd=diameter(t.right)
            lh=Depth(t.left)
            rh=Depth(t.right)
        return max(lh+rh+1,max(ld,rd))
    
    return diameter(p)

def weightedroadlength(T): #T5
    if T.IsEmpty(): return
    p=T._root
    q=[p]
    l=[]
    ps,cs,i=1,0,0
    sum=0
    while True:
        p=q.pop(0)
        if p.left is not None:
            q.append(p.left)
            cs+=1
        if p.right is not None:
            q.append(p.right)
            cs+=1
        
        sum+=p.data*i
        ps-=1
        if ps==0:
            i+=1
            ps=cs
            cs=0
        if q:
            continue
        else:
            break
    return sum


maxnode=BinTreeNode(0)
maxsum=None
def maxsubtree(T):#T6
    if T.IsEmpty():
        print "False"
        return
    
    def subtree(t):
        global maxsum
        global maxnode
        if t==None:
            return 0
        leftsum=subtree(t.left)
        rightsum=subtree(t.right)
        sum=t.data+leftsum+rightsum
        if maxsum<sum:
            maxsum=sum
            maxnode=t
        return sum
    t=T._root
    subtree(t)
    print "the max sum is", maxsum
    print "the max root is",maxnode.data
    return

def keywordfind(T,b): #T7
    if T.IsEmpty(): return False
    a=b
    t=T._root
    tmp=a.pop(0)
    while t!=None:
        if tmp==t.data:
            if a: tmp=a.pop(0)
            else: break
            if t.left!=None and tmp==t.left.data:
                t=t.left
            elif t.right!=None and tmp==t.right.data:
                t=t.right
            else:
                return False
    return True



#def keyword(T,x):   #T7
#    t=T._root
#    b=[]
#    if t!=None:
#        tmp=t
#        while tmp!=None:
#            b.append(tmp.data)
#            if tmp.data==x:
#                return b
#            if tmp.data<x:
#                tmp=tmp.right
#            else:
#                tmp=tmp.left
#    return b
    
#A=[7,6,15,3,0,10,17,1,4,0,0,0,12,0,20]
#A=[10,5,12,7,0,0,4]
#A=[-4,-2,3,11,0,2,-5,-3,1,0,0,0,0,0,4]

#A=[40,30,65,25,35,50,0,10,26,33,0,0,0,0,0,0,0,0,27,0,0,0,0,0,0,0,0,0,0,0,0]
#t=BinTrLList(A)
#print t._root.left.data
#print IsBalaced(t)#T1
#print POrder(t) #T2
#roadco(t,22) #T3
#print treediameter(t) #T4
#print weightedroadlength(t) #T5
#maxsubtree(t) #T6
#b=[40,30,25,26,10]
#print keywordfind(t,b) #T7

