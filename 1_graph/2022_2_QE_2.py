'''
In this problem, given an acyclic directed graph G, you will implement function paths(G, s, t) 

that returns the list of all paths between two vertices s and t. 

A path between two vertices is also a list of vertices. 

Paths in the list can be in any order, and each element in the path (element in the inner list) should be the id (string) of the vertex


   a  -------> b 
   |           |
   |           |
   +           +
   c <-------- d 

result example [['a', 'c'], ['a','b','d','c']]
'''


# 문제의 특징을 보면, acyclic graph니까 tree인데, search이다. 
# bfs 혹은 dfs 인데, 

from collections import deque   

class GNode:
    def __init__(self, id):
        self.id = id  # id is a string 
    def __str__(self):
        return self.id 
    
'''bfs 를 이용, backtracking은 사용안함 
'''

def paths(G, s, t):
    # q is an linked list, python 에서 deque는 큐를 구현할 때 사용됨. 
    # q에는 (현재 노드, 현재까지의 path) 가 tuple의 형태로 저장됨. 
    # duque에 아이템을 삽입할 때 
    q = deque([(s, [s])])
    paths = []
    while q:
        cur, path = q.popleft()

        if cur == t:
            paths.append([x.id for x in path])
        for neighbor in G[cur]:
            if neighbor not in path:
                q.append((neighbor, path+[neighbor])) # (b,[a,b])->(d ,[a,b,d])
    return paths 

'''
dfs, backtracking사용 
dfs는 recursion을 이용한다는 것이 bfs와 가장 큰 차이점인 것 같다. 
둘 다 curNode의 neighbors들을 방문하는 것은 동일하다. 
'''
# a -> b 가면 다시 a로 가서 다른 neighbor에 가야함. 


# you don't need to use return keyword in this help function
# because it automatically upate path and paths list and the changes will affect the paths that you will return. 
def dfs_help(graph, cur, dest,visited,  path, paths):
    
    visited[cur] = True 
    path.append(cur.id)

    if cur == dest:
        # be careful you do the shallow copy which just copy the data not the pointer (address itself)
        # deepcopy: a new object in a new memory place is created. It means that any changes made to a copy of the object do not reflect in the original object. 
        # shallow copy: a reference of an object is copied into another object. It means that any changes made to a copy of an object do reflect in the original object 
        # path: store all the path 
        # paths: only store the result path that we want 
        paths.append(path[:]) # path[:] -> shallow copy 
    else:
        for node in graph[cur]:
            if visited[node] == False:
                dfs_help(graph, node, dest, visited, path, paths)
    
    path.pop()
    visited[cur] = False 
    
def paths(G,s,t):
    

    #INIT 
    visited = dict()
    for node in G:
        visited.setdefault(node, False)
    path = []
    answer = []

    dfs_help(G, s, t, visited, path, answer)

    return answer 



if __name__ == '__main__':
    a, b, c, d = GNode('a'), GNode('b'), GNode('c'), GNode('d')
    G = dict() 
    G[a], G[b], G[c], G[d] = [b, c], [d], [], [c]
    print(paths(G, a, c))