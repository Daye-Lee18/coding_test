from collections import deque 

#Node definition 
class GNode: 
    def __init__(self, id, color ='W', d=0, p=None):
        self.id = id # id is a string 
        self.color = color # color (status) of node 
        self.distance = d 
        self.parent = p
    def __str__(self):
        return self.id 

# problem (a) bfs(G,s)
# performs a BFS algorithms on a connected undirected graph G from the source node s 

def bfs(G,s):
    q = deque([s])

    while q:
        cur = q.popleft()

        for neighbor in G[cur]:
            if neighbor.color == 'W':
                q.append(neighbor)
                neighbor.color = 'G'
                neighbor.distance = cur.distance + 1
                neighbor.parent = cur
    return G, s
    

# problem (b) level_partition(G,s)
def level_partition(G,s) -> list:
    G, s= bfs(G, s) 

    levels = {}

    for node in G.keys():
        if node.distance not in levels:
            levels[node.distance] = []
        levels[node.distance].append(node.id)
    partition = list(levels.values())

    return partition
               
    





if __name__ == "__main__":
    r, s, t, u, v = GNode('r'), GNode('s'), GNode('t'), GNode('u'), GNode('v')
    w, x, y = GNode('w'), GNode('x'), GNode('y')
    G = dict()
    G[r], G[w], G[t], G[u], G[v] = [s, v], [s,t,x], [w, x, u], [t, x, y], [r]
    G[w], G[x], G[y] = [s, t, x], [w, t, u, y], [x, u]

    # for key, value in G.items():
    #     print(type(key))
    #     for v in value:
    #         print(v.id)
    # print(type(s))
    print(level_partition(G, s))

