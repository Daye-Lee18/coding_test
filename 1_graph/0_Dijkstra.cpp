/*
start와 dest가 있는 상황에서, shortest path 를 찾는 과정 
negative wieght이 없는 상황에서 사용 

모든 vertex를 돌면서 해당 VERTEX에 연결된 edge에 대해 relaxation한다.
 
 pseudo code 
 
 1  function Dijkstra(Graph, source):
 2      
 3      for each vertex v in Graph.Vertices:
 4          dist[v] ← INFINITY
 5          prev[v] ← UNDEFINED
 6          add v to Q
 7      dist[source] ← 0
 8      
 9      while Q is not empty:
10          u ← vertex in Q with min dist[u]
11          remove u from Q
12          
13          for each neighbor v of u still in Q:
14              alt ← dist[u] + Graph.Edges(u, v) // alt = the length of the path from the root node to the neighbor node v if it were to go through u 
15              if alt < dist[v]:
16                  dist[v] ← alt
17                  prev[v] ← u
18
19      return dist[], prev[]


*/