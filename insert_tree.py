class Node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.val=item
def insert(root,item):
    if root is None:
        v=Node(item)
        return v
    else:
        if root.val==item:
            return root
        elif root.val<item:
            root.right=insert(root.right,item)
        else:
            root.left=insert(root.left,item)
        return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
root=Node(2)
root.left=Node(1)
root.right=Node(1)
root.left.left=Node(0)
insert(root,7)
inorder(root)
