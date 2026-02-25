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

def search_BST_low(node): # Inorder Successor
    if node:
        if not node.left == None:
            search_BST_low(node.left)
        else:
            print(node.data)
            return node
search_BST_low(tree3)

# Zoom 33:

def search_BST_high(node):
    if node:
        if not node.right == None:
            search_BST_high(node.right)
        else:
            return node

def delete_node(node, key):
    if node is None:
        return node

    if node.data > key:
        node.left = delete_node(node.left,key)
    elif node.data < key:
        node.right = delete_node(node.right,key)
    else:
        # Case 1
        if node.left is None and node.right is None:
            return None
        # Case 2
        if node.right is None:
            return node.left
        elif node.left is None:
            return node.right
        # Case 3
        if node.right.data > key:
            temp = search_BST_low(node.right)
            node.data = temp.data
            node.right = delete_node(node.right,temp.data)
        elif node.left.data < key:
            temp = search_BST_high(node.left)
            node.data = temp.data
            node.left = delete_node(node.left,temp.data)

    return node

delete_node(tree3,15)
inorder(tree3)

tree4 = Node(56)
tree4.left=Node(47)
tree4.left.left=Node(32)
tree4.left.right=Node(52)
tree4.right=Node(78)
tree4.right.left=Node(68)
tree4.right.right=Node(98)
print("")
info = print("Write '-None-' to skip.")
while True:
    input1 = int(input("What should be inserted?"))
    insert(tree4,input1)
    input2 = int(input("What should be deleted?"))
    delete_node(tree4,input2)
    inorder(tree4)
    print("")


