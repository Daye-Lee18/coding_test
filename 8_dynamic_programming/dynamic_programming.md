# Dynamic Porgramming 

## Definition 
- an optimization technique to solve recursive problems more efficiently 
- find if there are repetitive subproblems 
- compute only once and stor the value (memoization) 

## When to use 
- if the problem can be divided into subproblems 
- If we can implement a recursive solution 
- There are repetitive subproblems 


## Approach 
- Memoization (top-down recursive approach)
- Tabulation (bottom-up iterative approach)
  
### Memoization example 

```python

memo = {} #dictionay for Memoization

def fib(n):
  if n == 0: # base case 1
    return 0
  if n == 1: # base case 2
    return 1
  elif n in memo: # Check if result for n has already been evaluated
    return memo[n] # return the result if it is available
  else: # otherwise recursive step
    memo[n] = fib(n-1) + fib(n-2) # store the result of n in memoization dictionary
    return memo[n] # return the value

print (fib(100))

```

### Tabulation example 

```python

def fib(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  # table for tabulation
  table = [None] * (n+1) 
  table[0] = 0        # base case 1, fib(0) = 0
  table[1] = 1        # base case 2, fib(1) = 1
  # filling up tabulation table starting from 2 and going upto n
  for i in range(2,n+1):  
    # we have result of i-1 and i-2 available because these had been evaluated already
    table[i] = table[i-1] + table[i-2]  
  # return the value of n in tabulation table
  return table[n]    

print(fib(100))

```

### Input-based & return-based recursion 

- 문제: 
  - binary tree가 있을 때 
  - input : binary tree의 root 노드 
  - return: pre-order depth-first traversal 수행 후, 방문한 순서대로 노드의 val을 나열한 list 
    - root 가 없는 경우는 empty list return 


#### Input-based recursion 
: recursive하게 불리는 function parameter (input)를 최종 return 값으로 함 

```python

def preorderTraversal(root: TreeNode) -> List[int]:

  def helper(cur: TreeNode, output: list):
    if cur == None: # base case 
      return 

    output.append(cur.val) # visit function 

    # recursive call from left to right 
    helper(cur.left, output)
    helper(cur.right, output) 

  if root == None:
    return []
  
  output = [] 
  helper(root, output)

  return output 


```

#### Return-based recursion 
: recursive하게 return 값에 add하여 최종 return 값을 정함 

```python 

def preorderTraversal(root: TreeNode) -> List[int]:
  if root == None:
    return []

  return [root.val] + preorderTraversal(cur.left) + preorderTraversal(cur.right) 


```