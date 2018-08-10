
import math as math
class LNode:
    def __init__(self,elem,next_=None):
        self.elem=elem
        self.next=next_

class LinkedListUnderflow(ValueError):
    pass

class LList:
    def __init__(self):
        self._head = None
        self._tail = None
    
    def is_empty(self):
        return self._head is None
    
    def prepend(self,elem):
        self._head=LNode(elem,self._head)
    
    def append(self,elem,add=None):
        if self._head is None:
            self._head=LNode(elem)
            self._tail=self._head
            return
        p=self._head
        while p.next is not None:
            p=p.next
        if add is not None:
            p.next=LNode(elem,add)
        else:
            p.next=LNode(elem)
            self._tail=p.next        
            
            #if add is not None:
            #    p.next=LNode(elem)
            #else:
            
    
    def shift(self):
        if self._head is None:
            raise LinkedListUnderflow("in shift")
        p=self._head
        #e=self._head.elem
        self._head=self._head.next
        return p
    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        p=self._head
        while p.next.next is not None:
            p=p.next
        q=p.next
        q.next=None
        p.next = None
        return q.elem

    def printall(self):
        p=self._head
        A=[]
        while p is not None:
            A.append(p.elem)
            p=p.next
        print A

def ration(N,M): #T1
    x=N/M
    y=N%M
    CList=LList()
    CList.append(x)
    B=[y]
    while True:
        x=y*10/M
        y=(y*10)%M
        B.append(y)
        if y==B[0]:
            CList.append(x)
            #CList.append(x,CList._head.next)
            return CList
        else:
            CList.append(x)        
    
def IsCircle(CList): #T2/T3
    f=s=CList._head
    i=0
    while f is not None and f.next is not None:
        if i==0:
            f=f.next.next
        elif i==1:
            f=f.next
        s=s.next
        if f is s:
            if i==0:
                i+=1
                f=CList._head
                print "This list has a circle"
            else:
                return f.elem
    return "This list does not have a circle"
def Change(List): #T4
    p=List._head
    while p is not None and p.next is not None:
        q=LNode(List.pop())
        temp=p.next
        p.next=q
        q.next=temp
        p=temp
    List.printall()

N=77
M=81
klist=ration(N,M)
klist.printall()
print IsCircle(klist)
lst=LList()
for i in range(10):
    lst.append(i)

lst.printall()
Change(lst)