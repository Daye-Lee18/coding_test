# dfs method 
def dfs(graph, v, visited):
    visited[v] = True 
    # you can do your own thing instead of print 
    print(v, end= ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

dfs(graph, 1, visited)

'''return-based & input-based solution'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 

# return  based 
def preorderTraversal(root:TreeNode) -> list:
    # base case 
    if not root:
        return []
            # visit function + recursive call + recursive call 
    return [root.val] + \
        preorderTraversal(root.left) +\
    preorderTraversal(root.right)

# input based 
def preorderTraversal(root:TreeNode) -> list:

    def helper(root:TreeNode, result:list):
        #base case 
        if not root:
            return

        result.append(root.val) # visit function 
        helper(root.left, result) # recursive call 
        helper(root.right, result)
    
    ans = []
    helper(root, ans)

    return ans 
