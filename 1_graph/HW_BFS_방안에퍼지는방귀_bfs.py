'''
input: M * N 리스트 

목표: 대각선 제외한 위, 아래, 위쪽, 오른쪽 으로 방귀가 퍼진 시간 구하기 
- 0: 빈 공간 
- 1: 방구 뀐 자리 
- -1 : 벽  

output: 퍼진 시간 
- 방귀가 방 전체로 퍼질 수 없으면 -1 return 
- 처음부터 방귀가 꽉 차 있으면 0을 return 

ex) 

room = [[-1, 1], [1, -1]] 
output = 0

room = [[1, -1, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0],
        [0, 0, 0, 0, -1, 0],
        [0, 0, 0, 0, -1, 1]]

output = 6

'''

'''
- deque를 이용한 bfs
- 방구의 시작 위치를 모두 돌고 -> 그(들)의 neigbhor를 돈다. (이를 통해 같은 level에 있는 애들은 같이 돌게 된다.)

'''


from typing import List
from collections import deque 

def BFS(room: List[List[int]]) -> int:
    
    # 방귀 위치 구하기 
    n_row = len(room)
    n_col = len(room[0])

    q = deque() 
    for i in range(n_row): # y 
        for j in range(n_col): # x 
            if room[i][j] == 1:
                q.append((i, j, 0)) # 현재 위치 (i,j)와 시작 시간인 1을 묶어서 저장 
    
    if len(q) == 0:
        return -1 
    
    # 방안 BFS 탐색 
    while q:
        start = q.popleft()

        if 0 <= room[start[0]][start[1]] <= 1 : # 현재 위치가 빈 공간 (0) 또는 방구의 위치 (1) 
            room[start[0]][start[1]] = start[2] # 방구 시간 update 

            # 위 , 아래, 오른, 왼
            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]

            for i in range(len(dx)):
                ax = start[0] + dx[i]
                ay = start[1] + dy[i]

                # 비어있는 공간인 경우 bfs 진행 
                # 새로운 위치가 그리드 내에 있고 빈 공간 (0) 인 경우에만 진입 
                if 0 <= ax < n_row and 0 <= ay < n_col and room[ax][ay] == 0:
                    q.append((ax, ay, start[2]+1))


    # 최종 답 
    ans = 0
    for i in range(n_row):
        for j in range(n_col):
            if room[i][j] == 0:
                return -1
            elif room[i][j] > 0:
                ans = max(ans, room[i][j])
    
    return ans







