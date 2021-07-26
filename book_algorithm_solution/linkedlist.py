class Node:
    def __init__(self,name,nextNode):
        self.name = name
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.pointer = None

    def insert(self,newnode):
        if self.pointer == None:
            self.pointer = newnode
            return
        else:
            newnode.nextNode = self.pointer
            self.pointer = newnode

    def printList(self,node):
        res = ""
        if node.nextNode == None:
            print(node.name)
        else:
            while not node == None:
                res += "->" + node.name
                node = node.nextNode
                print(res)

names = ['yamamoto','watanabe','ito','takahashi','tanaka']
llist = LinkedList()

for name in names:
    #print(f'name={name}')
    node = Node(name,None)
    llist.insert(node)
    llist.printList(node)

