class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(6)
root.left=Node(5)
root.right=Node(1)
root.left.left=Node(3)
root.left.right=Node(2)

def preorder(node):
    if node:
        print(node.data,end="-")
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data,end="-")

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data,end="-")
        inorder(node.right)

preorder(root)
print("")
postorder(root)
print("")
inorder(root)
print("")

total = 0
def count_nodes(node):
    global total
    if node:
        count_nodes(node.left)
        count_nodes(node.right)
        total += 1
count_nodes(root)
print(total)
print("")

def find_in_node(node,search):
    if node:
        find_in_node(node.left,search)
        find_in_node(node.right,search)
        if node.data == search:
            print(f"Data found in Tree.")
find_in_node(root,1)
print("")


root2 = None

def insert(root2,key):
    if root2==None:
        return Node(key)
    
    if root2.data > key:
        root2.left=insert(root2.left,key)
    else:
        root2.right=insert(root2.right,key)
    
    return root2

root2=insert(root2,8)
root2=insert(root2,12)
root2=insert(root2,10)
root2=insert(root2,3)
root2=insert(root2,6)

inorder(root2)
print("")

def search_BST(node,key):
    #find an element in BST
    if node:
        #print(node.data)
        if node.data > key:
            search_BST(node.left, key)
        elif node.data < key:
            search_BST(node.right,key)
        elif node.data == key:
            print("Data Found in Tree")

tree3 = Node(18)
tree3.left=Node(12)
tree3.left.left=Node(6)
tree3.left.right=Node(15)
tree3.right=Node(24)
tree3.right.left=Node(20)
tree3.right.right=Node(28)

search_BST(tree3,6)

def search_BST_low(node):
    if node:
        if not node.left == None:
            search_BST_low(node.left)
        else:
            print(node.data)
search_BST_low(tree3)


















