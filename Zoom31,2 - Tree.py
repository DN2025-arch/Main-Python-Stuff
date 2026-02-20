
#A tree is made of many nodes with two children nodes underneath.
class Node():
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
    def display(self):
        print(self.data)
        if not self.lchild == None:
            self.lchild.display()
        if not self.rchild == None:
            self.rchild.display()

Root = Node("Bird")
Root.lchild = Node("Nest")
Root.rchild = Node("Branch")
Root.lchild.lchild = Node("Egg")
Root.lchild.rchild = Node("Worm")
Root.rchild.lchild = Node("Roots")
Root.rchild.rchild = Node("Leaves")

Root.display()
