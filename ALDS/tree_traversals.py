# tree traversals implementation
#
# inorder - left > root > right
# preorder - root > left > right
# postorder - left > right > root
# code from geeksforgeeks

class Node :
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)

def printPreorder(root):
    if root:
        print(root.val)
        printPreorder(root.left)
        printPreorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("inorder")
printInorder(root)
print("preorder")
printPreorder(root)
print("postorder")
printPostorder(root)