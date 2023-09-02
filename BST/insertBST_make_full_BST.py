'''
BST에서는 left.val < root.val < right.val 임으로 항상 기억 
'''

from BST_Helper import *

def P3(root: TreeNode, val: int) -> TreeNode:    
    ##### Write your Code Here #####
    # coutNode함수: subtree의 노드 수를 세는 함수 (recursive)
    def countNode(head):
        if head is None:
            return 0
        return 1 + countNode(head.left) + countNode(head.right) 
    
    #Helper function
    def _insert(head, val): 
        # head가 None이면 val값을 지닌 TreeNode 생성하여 반환 
        if head is None:
            return TreeNode(val)
        # head가 None이 아니면 head의 left와 right 트리의 노드 수를 세고 head의 값을 rootVal로 둠
        lCnt = countNode(head.left)
        rCnt = countNode(head.right)
        rootVal = head.val
        
        # Base case: left나 right child 중 하나가 None일 경우
        if lCnt == 0: # left가 None일 경우: root vs. right node vs. target val 을 비교            
            rVal = head.right.val # rVal: head의 right 노드의 val
            if val > rVal: # insert하려는 val이 rVal보다 크면) head의 left: rootVal을 val로 가진 노드 / head의 val: rVal / head의 right의 val: val
                head.left = TreeNode(rootVal)
                head.val = rVal
                head.right.val = val
            elif val > rootVal: # val이 rootVal보다는 크고 rVal보다는 작으면) head의 left: rootVal을 val로 가진 노드 / head의 val: val
                head.left = TreeNode(rootVal)
                head.val = val
            else: # val이 rootVal보다 작으면)  head의 left: val 노드
                head.left = TreeNode(val)
            return head

        elif rCnt == 0: # right가 None일 경우           
            lVal = head.left.val
            if val > rootVal:
                head.right = TreeNode(val)                
            elif val > lVal:
                head.right = TreeNode(rootVal)
                head.val = val
            else:
                head.right = TreeNode(rootVal)
                head.val = lVal
                head.left.val = val           
            return head
        
        # left subtree에 더 많은 수의 노드가 있으면 right subtree에 삽입하고 반대의 경우에는 반대로
        # root 에 child tree가 둘 다 있는 경우에는 target val 과 root의 value만 비교해서 그 아래 트리에 insert하면 된다. 
        if lCnt > rCnt:
            if val > rootVal:                
                head.right = _insert(head.right, val)
            # left subtree가 full인데, val이 root의 값보다 작을 때
            else:            
                #left subtree에서 가장 큰 값을 찾기 (lCnt > rCnt 상황에서 root가 될 수 있는 candidate = left subtree의 largest )
                pOfLargest = head.left
                largest = head.left
                while largest.right is not None:
                    pOfLargest = largest
                    largest = largest.right            
                    
                if val < largest.val: # val이 left subtree에서 가장 큰 값보다 작은 경우               
                    # head의 val를 left subtree에서 가장 큰 값으로 바꾸고 head의 left에는 val을 right에는 rootVal을 삽입 
                    head.val = largest.val                
                    pOfLargest.right = None
                    head.left = _insert(head.left, val)
                    head.right = _insert(head.right, rootVal)
                else: # val이 left subtree에서 가장 큰 값보다 큰 경우 
                    # val이 head의 val값이 되고 본래 rootVal은 right subtree에 삽입
                    head.val = val
                    head.right = _insert(head.right, rootVal)                
        else:
            # right subtree가 full인데 val이 root값보다 큰 경우
            if val > rootVal:
                #right subtree에서 가장 작은 value를 찾기
                pOfSmallest = head.right             
                smallest = head.right
                while smallest.left is not None:
                    pOfSmallest = smallest
                    smallest = smallest.left                    
                
                if val > smallest.val:  # val이 right subtree에서 가장 작은 값보다 큰 경우
                    # smallestNode 가 새로운 head가 됨
                    head.val = smallest.val
                    pOfSmallest.left = None                    
                    head.right = _insert(head.right, val)
                    head.left = _insert(head.left, rootVal)
                else: # val이 right subtree에서 가장 작은 값보다 작은 경우
                    # val이 head의 val이 되고, 본래 head의 val은 left subtree에 삽입 
                    head.val = val                                       
                    head.left = _insert(head.left, rootVal)
                    
            # left subtree가 비어 있고 val이 root값보다 작을 때
            else:
                head.left = _insert(head.left, val)
        return head
        
    _insert(root, val)
    return root