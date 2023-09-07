
'''
input: string s 
output: the longest palindromic subsequence's length 

s = "bbbab" , output = 4 ('bbbb')
s - 'cbbd' , output = 2 

'''

import functools 

'''top-down approach''' 
# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
        
#         # dp(i, j) := LPS's length is s [i...j]
#         @functools.lru_cache(None) # functools.lru_cache() 는 함수의 결과를 캐시해 주는 함수 데커레이터입니다. 같은 인수를 전달했던 호출 결과가 이미 캐시되어 있으면 함수를 실행하지 않고 캐시 결과를 반환합니다.

#         def dp(i: int, j:int) -> int:
#             if i > j:
#                 return 0
#             if i == j :
#                 return 1 
#             if s[i] == s[j]:
#                 return 2 + dp(i+1, j-1)
            
#             return max(dp(i+1, j), dp(i, j-1))
        
#         return dp(0, len(s) -1)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # create a memoization dictionary 
        memo = {}

        def dp(i: int, j :int) -> int:
            if i > j:
                return 0
            if i == j:
                return 1 
            if (i, j) in memo:
                return memo[(i, j)]
            
            if s[i] == s[j]:
                memo[(i, j)] = 2 + dp(i+1, j-1)
            else:
                memo[(i, j)] = max(dp(i+1, j), dp(i, j-1)) # max함수를 써서 둘 중에 큰 것을 사용하는 것이 포인트! 현재 두 char가 같지 않으면 왼쪽 포인터를 옮기거나 오른쪽 포인터를 옮기거나 2가지 option이 있기 때문에 
            
            return memo[(i, j)]
        
        return dp(0, len(s) -1 )


'''bottom-up approach'''
class Solution:
  def longestPalindromeSubseq(self, s: str) -> int:
    n = len(s)
    # dp[i][j] := LPS's length in s[i..j]
    # LPS = longestPalindromeSubseq 의 acronym
    dp = [[0] * n for _ in range(n)] # n * n matrix 

    for i in range(n):
      dp[i][i] = 1

        
    # (0,0) (0,1) (0,2)   
    # (1,0) (1,1) (1,2)
    # (2,0) (2,1) (2,2)           

    # (0,0)    
    # (1,0) (1,1) 
    # (2,0) (2,1) (2,2)  
     
    # n = matrix 크기 n*n 
    # i = row index 
    # j = col index 
    # d = 반절 매트릭스에서 col의 길이 예를 들어, col=0일때 row index는 3-1 (2까지 존재)
    for d in range(1, n): # col (0,0)은 이미 1이므로 range(1) 부터 시작 
      for i in range(n - d): # row (반절) 
        j = i + d # j는 col의 끝에서부터 비교 
        if s[i] == s[j]:
          dp[i][j] = 2 + dp[i + 1][j - 1]
        else:
          dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]



if __name__ == '__main__':
    s = "bbbab"
    x = Solution()
    print(x.longestPalindromeSubseq(s))