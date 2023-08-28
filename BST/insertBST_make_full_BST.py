from BST_Helper import *

def swap(&a: TreeNode, &b: TreeNode )

def min_heapify(root:TreeNode):
    largest = root 
    if root.left.val > root.val:
        largest = root.left 
    if root.right.val > root.val:
        largest = root.right 
    
    if largest != root:
        swap(largest, root)

def P3(root: TreeNode, val: int) -> TreeNode:
    # insert node into a tree 
    myTree = BST(root) 
    myTree.insert(val)

    # rebuild the complete binary tree 
    # make min-heap 
