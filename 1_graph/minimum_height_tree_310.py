'''
input: edges [[0,1], [1,3], [3, 4], [4,0]]

output: 특정 node를 root했을 때 가장 height이 짧은 node의 list

ex) 
   3                        
/ | | \
0 1 2 4 
      |
      5
답 : [3, 4] 
'''

import collections 
from typing import List 

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        # make graph 
        graph = collections.defaultdict(set)

        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        leaves =[]
        # erase leaves first 
        for key, childrens in graph.items():
            if len(childrens) == 1 :
                leaves.append(key)
        
        # 차례대로 leaves 지워나가기 (맨 아래에서 제일 작은 children 지우고 위로 가면서 지우다보면, 가장 위의 node(s) 들이 살아남게 된다!)
        # 옆의 예시에서는 0, 1, 2, 5 지워지고 3 --edge-- 4 가 남는데, n 이 2보다 크지 않으므로 while문을 나오게 된다. 
        while n > 2:
            n -= len(leaves)
            new_leaves =[]
            for leave in leaves:
                # for neighbor in graph[leave]: // set의 size가 변해서 이렇게는 안됨 
                neighbor = graph[leave].pop() # leave입장에서 neighbor지움  
                graph[neighbor].remove(leave) # neighbor 입장에서 leave 지움 
                    
                if len(graph[neighbor]) == 1 :
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves     
