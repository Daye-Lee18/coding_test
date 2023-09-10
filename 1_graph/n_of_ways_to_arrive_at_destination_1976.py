'''
input: # of nodes , list with element [u, v, time], undirected graph 
    - note: undirected graph라서 visited data 가 추가적으로 필요할 것 
output: the number of ways you can arrive at your destination in the shortest amount of time 


ex) 


'''


'''아래코드는 왜 이상하게 나올까'''
import heapq 

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        # make adjacency graph 
        # [(0, 1, time_cost).....] -------->   [0: [(1, time_cost), (3, time)], 1: [(0, time), (4, time) ] ...] 형태로 변환 
        '''
        이렇게 안해도 roads[0][0] 으로 바로 cost element에 access할 수 있다. 
        
        '''
        graph = dict()
        for edge in roads:
            if edge[0] not in graph:
                graph[edge[0]] = [(edge[1], edge[2])]
            if edge[1] not in graph:
                graph[edge[1]] = [(edge[0], edge[2])]
            if edge[0] in graph:
                graph[edge[0]].append((edge[1], edge[2]))
            if edge[1] in graph:
                graph[edge[1]].append((edge[0], edge[2]))

        def helper(graph: list, visited: list, curNode: int, total_cost: int, path: list, paths:list) -> None:
            if curNode == n-1:
                if total_cost not in paths:
                    paths[total_cost] = 1 
                else:
                    paths[total_cost] += 1
                return 

            #dictionary 
            #key: value = time spent : count 
            for neighbor, cur_cost in graph[curNode]:
                if not visited[neighbor]:
                    total_cost += cur_cost  
                    visited[neighbor] = True 
                    helper(graph, visited, neighbor, total_cost, path, paths)
                    total_cost -= cur_cost
                    visited[neighbor] = False 

        visited = [False for _ in range(n)]
        path = []
        paths = dict() 
        helper(graph, visited, 0,0,path, paths)
        # print(paths)
        cost_list = list(paths) # key 값만 저장된 list가 됨 
        # print(paths)
        min_cost = heapq.heappop(cost_list)
        
        return paths[min_cost]