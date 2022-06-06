#binary search tree implementation
#
#left child is smaller than parent, right child is bigger than parent
#code from geeksforgeeks

def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def min_val(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

def delete(root, key):
    if root is None:
        return root
    if key < root.val:
        root.left = delete(root.left, key)
    elif(key > root.val):
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = min_val(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)
    return root

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
inorder(r)
print ("\nDelete 20")
r = delete(r, 20)
print ("Inorder traversal of the modified tree")
inorder(r)
 
print ("\nDelete 30")
r = delete(r, 30)
print ("Inorder traversal of the modified tree")
inorder(r)
 
print ("\nDelete 50")
r = delete(r, 50)
print ("Inorder traversal of the modified tree")
inorder(r)