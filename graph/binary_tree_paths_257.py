'''
Backtracking 문제 

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List 
from collections import deque 


'''

아래의 방식은 bfs로 구현한것으로 backtracking개념은 사용하지 않았다. 
backtracking 이란 문제에서 요구하는 모든 경우의 수를 계산하기 위해 한번 갔던 길을 되돌아가는 것으로 이때 이 전 상황으로 초기화? 시켜주는 것이 중요하다. 
'''
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # INIT 
        q = deque([root, []])
        visited = dict()
        visited[root] = False 


        while q:
            cur, path = q.popleft() 

            if cur.left not in visited:
                q.append(cur.left)
                visited[cur.left] = True 
            if cur.right not in visited:
                q.append(cur.right)
                visited[cur.right] = True 


'''
dfs, backtracking으로 구현 

   1
  / \
  2  3 
   \
    5
'''

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        def dfs_help(cur, visited, path, paths):
            if cur != None:
                visited[cur] = True 
                
                # your algorithm 
                path.append(str(cur.val))
                # child node 
                if cur.left == cur.right == None: 
                    paths.append("->".join(path)) 
                else:    
                    # neighbors 
                    # if visited[cur.left] == False: 
                    if cur.left not in visited: 
                        dfs_help(cur.left, visited, path, paths)
                    if cur.right not in visited:
                        dfs_help(cur.right, visited, path, paths) 
                # backtracking 
                # if you don't do backtracking, you would get the answer of ["1->2->5","1->2->5->3"] which 2-> 5-> is incorrect in 2nd path answer 
                # In this case, if you hit 5 you will hit the below code line. and cur would be 5 and then 2 and then 1 
                path.pop()
                visited[cur] = False # 사실 여기서 이 부분은 없어도 알고리즘이 돌아가고 path.pop()을 해주는 것이 backtracking에서 핵심이다. 

        # INIT 
        path = []
        paths = []
        visited=dict() 

        dfs_help(root, visited, path, paths) 

        return paths