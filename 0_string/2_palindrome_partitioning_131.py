# https://takeuforward.org/data-structure/palindrome-partitioning/

'''
It's also backtracking problem 


input : s 
목적: partition s such that every substring of the partition is a palidrome 
return: all possible palindrome partitioning of s 

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

        # def is_palindrome(s:str, start:int, e:int) -> bool:

        #     while start <= e and s[start] == s[e] :
        #         start += 1 
        #         e -= 1 
            
        #     return True if start > e else False
        
        partitionHelper(0)
        return res 
    




















































