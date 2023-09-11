from collections import deque

# Helper functions: DO NOT MODIFY!!

# Definition for Node of singly linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TreeNode class (printTree function)
# create_linked_bst function 
# BST class (search, insert, delete)
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None 
        self.right = None
          
    def printTree(self) ->list:
        # level-order traversal 
        result = []
        thislevel = [self] # initialize the list with the current instance of a tree node 
        
        while thislevel:
            nextlevel = []
            all_none = True #flag to check if all nodes in this level are None or leaf nodes 


            # none_list=1
            # for n in thislevel:
            #     if n !=None:
            #         none_list=0
            #         break
            # if none_list==1:
            #     return result

            # iterate and add childrens into nextlevel list      
            for n in thislevel:
                if n is not None: 
                    result.append(n.val)
                    nextlevel.append(n.left)
                    nextlevel.append(n.right)
                    if n.left is not None or n.right is not None :
                         all_none = False # Set the flag to False if non-leaf node is encountered 
                else:
                    result.append(None)
                    nextlevel.append(None)
                    nextlevel.append(None)

            if all_none:
                 return result 

            # update thislevel    
            thislevel = nextlevel
        return result

def create_linked_bst(arr: list) -> TreeNode:
    if len(arr) < 1: return None
    
    #creates and returns an iterator object n
    iterator_n = iter(arr) # convert an iterable object into an iterator 
    tree = TreeNode(next(iterator_n)) # return the first element 
    fringe = deque([tree])
    
    while True:
        head = fringe.popleft()
        try:
            l = next(iterator_n)
            head.left = TreeNode(l) if l != None else None
            fringe.append(head.left)

            r = next(iterator_n)
            head.right = TreeNode(r) if r != None else None
            fringe.append(head.right)
            
        except StopIteration:
            break
    return tree

class BST():
    def __init__(self, root:TreeNode) -> None:
        self.root = root
        
    ### search ###
    def __searchHelp(self, curNode: TreeNode, x: int) -> TreeNode:
        if not curNode: # current node가 leaf에 밑에 있는 애면
            return None
        if x == curNode.val:
            return curNode
        
        if x < curNode.val:
            return self.__searchHelp(curNode.left, x)
        else:
            return self.__searchHelp(curNode.right, x)
        
    def search(self, x:int) -> TreeNode:
        return self.__searchHelp(self.root, x)
    
    ### insert ###
    def __insertHelp(self, curNode: TreeNode, x: int) -> TreeNode:
        # when leaf node is reached
        if not curNode:
            # this leaf node is reached by moving right or left from its parent node,
	        # and the return value here is assigned as parent's right or left node    
            return TreeNode(x)
        
        # (2) Recursive case
        if x < curNode.val:
            curNode.left = self.__insertHelp(curNode.left, x)
        elif x > curNode.val: 
            curNode.right = self.__insertHelp(curNode.right, x)
        
        # if x == curNode.val
        return curNode
    
    def insert(self, x: int) -> None:
        # tree is changed when inserted
        self.root = self.__insertHelp(self.root, x)
    
    ### delete ###
    def __findMax(self, curNode: TreeNode) -> int:
        # When you can't move more to the right, return the value of curNode
        if not curNode.right:
            return curNode.val
        # When you can move more to the right, keep looking for the node with max value
        else:
            return self.__findMax(curNode.right)
    
    def __deleteHelp(self, curNode: TreeNode, x: int) -> TreeNode:
        if not curNode:
            return None
        
        if x < curNode.val:
            # left subtree는 이제 left subtree에서 x를 삭제한걸로 대체
            curNode.left = self.__deleteHelp(curNode.left,x)
        elif x > curNode.val:
            # right subtree는 이제 right subtree에서 x를 삭제한걸로 대체
            curNode.right = self.__deleteHelp(curNode.right,x)
        # x == curNode.val
        else: 
            # (1) No child -> replace curNode with None
            if curNode.left == None and curNode.right == None:
                return None # self.root update 해줄 값 
            
            # (2) One child -> replace curNode with the child
            elif curNode.left == None and curNode.right:
                return curNode.right # self.root update 해줄 값 
            elif curNode.left and curNode.right == None:
                return curNode.left # self.root update 해줄 값  
            
            # (3)  Two children
            # replace curNode with the node that has either
            # [a] the biggest value from its left subtree, or
            # [b] the smallest value from its right subtree
            # Here, choose and implement method [a]
            else:
                leftLargest = self.__findMax(curNode.left) #제일 큰 애 찾아서
                curNode.left = self.__deleteHelp(curNode.left, leftLargest) #leftlargest삭제한 걸로 left-tree 업데이트
                curNode.val = leftLargest #현재 노드값만 leftLargest로 변경
            
        return curNode # self.root update 해줄 값 
        
    def delete(self, x:int) -> None:
        # root may change when some node is erased 
        self.root = self.__deleteHelp(self.root, x)


if __name__ == '__main__':
    tree1 = TreeNode(1)
    tree2 = TreeNode(2)
    tree3 = TreeNode(3)
    tree4 = TreeNode(4)
    tree5 = TreeNode(5)
    tree6 = TreeNode(6)
    tree7 = TreeNode(7)
    
    '''
        4
       /  \ 
      2    6
    /  \  /  \
   1   3 5    7
   '''

    tree4.left = tree2
    tree4.right = tree6

    tree2.left = tree1
    tree2.right = tree3

    tree6.left = tree5
    tree6.right = tree7

    # Instance of class BST, setting node with value of 4 as its root
    myTree = BST(tree4)

    # Test search
    node = myTree.search(6)
    if node == None:
        print(node)
    else:
        print(node, node.val)

    # Test Insert
    myTree.insert(8)
    node = myTree.search(8)
    if node == None:
        print(node)
    else:
        print(node, node.val)

    # Test delete
    print("root:", myTree.root.val)

    #print tree 
    print(myTree.root.printTree()) # [4, 2, 6, 1, 3, 5, 7, None, None, None, None, None, None, None, 8]

    myTree.delete(4)
    print("new root:", myTree.root.val) 

    # 이 경우에는 rebuild가 되지 않음 
    print(myTree.root.printTree()) # [3, 2, 6, 1, None, 5, 7, None, None, None, None, None, None, None, 8]

    print("Is there node with the value of 4?")
    node = myTree.search(4)
    if node == None:
        print(node)
    else:
        print(node, node.val)