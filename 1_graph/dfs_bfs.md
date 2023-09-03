# BFS와 DFS의 차이 

- Graph에서 방귀 diffusion 문제를 생각해보면 
- 같은 level의 node들이 먼저 계산이 되어야지 다음 node를 계산할 수 있다. 
- 예를 들어, 퍼진 시간 2를 먼저 계산해야 3을 계산할 수 있음 
- 반면 dfs의 경우에는 섬을 생각해보면, 하나 다 계산하고 다음 계산해야하는 경우에 특수하게 사용된다. 
- 그 외의 경우에는, dfs와 bfs 모두 사용가능한 듯 하다. 