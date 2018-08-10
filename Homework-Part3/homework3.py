class Stack:                ##没有初始化的结构
    def __init__(self):     ##初始化-》成为实例
        self.list=[]

    def IsEmpty(self):      ##隐藏实现
        if len(self.list)==0:
            return True
        else:
            return False
    
    def Push(self,x):
        self.list.append(x)
    
    def Pop(self):
        if not self.IsEmpty():
            return self.list.pop(len(self.list)-1)
        else:
            return None
    
    def Top(self):
        if not self.IsEmpty():
            return self.list[len(self.list)-1]
        else:
            return None
    def printstack(self):     
        print self.list
    #def Len(self):
    #    return len(self.list)

def changestack(S1,S2): #T3
    #l=S1.Len()
    tmp=S1.Pop()
    while True:
        if tmp>S2.Top() or S2.IsEmpty():
            S2.Push(tmp)
            if S1.IsEmpty():break
            tmp=S1.Pop()
        elif tmp < S2.Top():
            S1.Push(S2.Pop())
        
    S2.printstack()

def changestack2(S): #T4
    if S.IsEmpty():
        return
    top1=S.Pop()
    if not S.IsEmpty():
        changestack2(S)  
        top2 = S.Top()  
        if top1 < top2:
            S.Pop()
            S.Push(top1)
            S.Push(top2)
            changestack2(S)
            return S
    S.Push(top1)

def changeorder(S): #T5
    if S.IsEmpty():
        return
    top1 = S.Pop()
    if not S.IsEmpty():
        changeorder(S)
        top2=S.Pop()
        changeorder(S)
        S.Push(top1)
        changeorder(S)
        S.Push(top2)
        return S
    S.Push(top1)
    

S1=Stack()
S2=Stack()
L=[2,5,6,7,4,8,9,3,1,0]
for a in L:
    S1.Push(a)
#changestack(S1,S2)
S2=changeorder(S1)
S2.printstack()