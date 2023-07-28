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
dfs, backtrackgng으로 구현 
'''