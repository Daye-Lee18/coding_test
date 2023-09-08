'''
input: m*n list

문제 조건:  
- 리스트는 0/1로 이루어져 있음 
- 1 은 땅, 0은 물 
- 물로 둘러싸여 있는 지역이 섬이다. 
- 상, 하, 좌, 우가 인접한 경우 

output: 섬의 개수 

ex) 

world = [[1, 1, 1, 1, 0],
        [1, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0]]

output = 1 

world = [[1,1,0,0,0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1]]
output = 3 
'''

'''

dfs recursion -> neighbor 방문 
'''
from typing import List

   
def ComputeIslandNum(world: List[List[int]]) -> int:

    def dfs(world, visit, n_row, n_col, i, j): 
        if 0 <= i < n_row and 0 <= j < n_col and visit[i][j] == False:
            # visit 
            visit[i][i] = True

            # do whatever you want 
            dfs(world, visit, n_row, n_col, i+1, j) 
            dfs(world, visit, n_row, n_col, i-1, j)
            dfs(world, visit, n_row, n_col, i, j+1) 
            dfs(world, visit, n_row, n_col, i, j-1)  

    n_row = len(world)
    n_col = len(world[0])

    ans = 0
    visit = [[False for _ in range(n_col)] for _ in range(n_row)]

    for i in range(n_row):
        for j in range(n_col):
            # 처음 방문한 땅이면 개수 추가 
            if world[i][j] == 1 and visit[i][j] == False:
                ans += 1 
                dfs(world, visit, n_row, n_col, i, j)

    return ans 