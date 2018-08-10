class LCList:
    def __init__(self):
        self._rear=None
    
    def is_empty(self):
        return self._rear is None

    def prepend(self,elem):
        p=LNode(elem)
        if self._rear is None:
            p.next_=p
            self._rear=p
        else:
            p.next_=self._rear.next_
            self._rear=self._rear.next_

    def append(self,elem):
        self.prepend(elem)
        self._rear=self._rear.next_
    
    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow("in pop of CLList")
        p=self._rear.next_
        if self._rear is p:
            self._rear = None
        else:
            self._rear = p.next_
        return p.elem
    def printall(self):
        if self.is_empty():
            return
        p=self._rear.next_
        while Ture:
            print p.elem
            if p is self._rear:
                break
            p=p.next_
