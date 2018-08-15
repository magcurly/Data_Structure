import re

class Node:
    def __init__(self,data,subs=[]):
        self._data=data
        self._child=list(subs)
    
    def GetData(self):
        return self._data
    
    def getchild(self):
        chda=[]
        for i in self._child:
            chda.append(i.data)
        return chda
    
    def setchild(self,node):
        self._child.append(node)

class Tree:
    def __init__(self):
        self._root=None
    
    def IsEmpty(self):
        return self._root is None
    
    def get_root
    def set_root(self,data):
        self._root=Node(data)

    def set_child(self,subtree):
        self._root._child.append(subtree)
    

def lca(tree,node):
    tree.get_root
            
    
def read_taxo_node(node_file):
    f=open(node_file,'r')
    for line in f:
        line=line.strip('\n')
        arr=line.split('\s*|\s*')
        
        t.setchild(arr[])