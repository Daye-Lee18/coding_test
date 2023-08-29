from BST_Helper import *

def P1(root: TreeNode, low: int, high: int) -> int:
    ans = 0

    
    def P1_help(cur: TreeNode, low:int, high:int, ans:int) -> int:
        if cur == None:
            return 0 
        
        else:
            if cur.val >= low and cur.val <= high:
                ans = ans + cur.val + P1_help(cur.left, low, high, ans) + P1_help(cur.right, low, high, ans)
            elif cur.val < low:
                ans = ans + P1_help(cur.right, low, high, ans) 
            # cur.val > high
            else:
                ans = ans + P1_help(cur.left, low, high, ans)
            
            return ans 

    return P1_help(root, low, high, ans)

# def P1(root: TreeNode, low: int, high: int) -> int:
#     ans = 0
#     if root == None:
#         return 0
#     else:
#         # if root.val is in range
#         if low <= root.val <= high:
#             # sum root value and left, right subtree
#             ans += root.val + P1(root.left, low, high) + P1(root.right, low, high)
#         # if root.val is smaller than low
#         elif root.val < low:
#             # Sum right subtree's values
#             ans += P1(root.right, low, high)
#         # if root.val is greater than high
#         else:
#             # Sum left subtree's values
#             ans += P1(root.left, low, high)
        
#     return ans

if __name__ == '__main__':
    root = create_linked_bst([10, 5, 15, 3, 7, 9, 18])
    print(P1(root, 3, 9)) # 15 
    
    
    
    

