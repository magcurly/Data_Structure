class Node:
    def __init__(self,data,b=[]):
        self.data=data
        self.child=b
    
    def GetData(self):
        return self.data
    
    def getchild(self):
        chda=[]
        for i in self.child:
            chda.append(i.data)
        return chda
    
    def setchild(self,node):
        self.child.append(node)

#class Tree:
    
def read_taxo_node(node_file):
    f=open(node_file,'r')
