# https://takeuforward.org/data-structure/palindrome-partitioning/

'''
 It's also backtracking problem 
''' 

from typing import List 

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        # argument: index = the position to partition the input string 
        def partitionHelper(index: int):
            if index == len(s):
                res.append(path[:])
                return 
            for i in range(index, len(s)):
                if isPalindrome(s, index, i):
                    path.append(s[index:i+1]) # a
                    partitionHelper(i+1)
                    path.pop() # pop every path that are in path list whenever the function in the stack is removed 
            
        
        def isPalindrome(s: str, start: int, end: int) -> bool:
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        partitionHelper(0)
        return res 
    




















































