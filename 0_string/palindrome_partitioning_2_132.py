import heapq


'''dynamic programming'''
# Time : O(MN)
# Space: O(MN)

class Solution:
    def minCut(self, s: str) -> int:
        
        # INIT 
        len_s = len(s) 
        cut = [0] * len_s 
        table  = [[False] * len_s for _ in range(len_s)]

        # Bottom-up approach 
        for end in range(len_s):
            mini = end 
            for start in range(end+1):
                # check if s[start:end+1] is a palindrome 
                # start + 1 > end -1 인 경우에는 start == end 인 경우 즉, substring이 character인 경우에는 무조건 palindrome이다. 혹은, table[start+1][end-1]
                if s[start] == s[end] and ( start + 1 > end -1 or table[start+1][end-1]): # table[start+1][end-1] = check if the previous string is palindrome 
                    table[start][end] = True 
                    mini = 0 if start == 0 else min(mini, cut[start-1] + 1)
            cut[end] = mini
        
        return cut[len_s-1]


'''
아래거는 time limit 초과로 안되는데, 답은 나올 것 같긴 하다. 
'''
# class Solution:
#     def minCut(self, s: str) -> int:
        
#         paths = []
#         path = []
#         heap = []
#         # global cut
#         cut = 0

#         def partition_helper(index:int, cut:int):

#             if index == len(s):
#                 # paths.append(path[:])
#                 # heapq.heappush(heap, (cut, path[:])) # memory limit exceeded 
#                 heapq.heappush(heap, cut)
#                 return 

#             for i in range(index, len(s)):
#                 if is_palindrome(s, index, i):
#                     cut += 1 
#                     path.append(s[index:i+1])
#                     partition_helper(i+1, cut)
#                     path.pop()
#                     cut -= 1 
                
        
#         def is_palindrome(s:str, start:int, end:int) -> bool:
#             while start <= end and s[start] == s[end]:
#                 start += 1 
#                 end -= 1 
            
#             return True if start > end else False 
        
#         partition_helper(0, cut)

#         min = heapq.heappop(heap)

#         return min -1 # return priority value not the key (data itself)


if __name__ == '__main__':
    s = 'aab'
    x = Solution()
    print(x.minCut(s)) # 1 