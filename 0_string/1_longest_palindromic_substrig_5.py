
'''
input = string s 
output : longest palindromic "substring" in s 

ex) 

s = "babad" 
output: "bab" or "aba" 

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        l = 0
        res  = ""
        max_len = 0 
        for mid in range(l, len(s)):
            l = r = mid # candidate length odd 
            while l >= 0 and r <len(s) and s[l] == s[r]:
                l -= 1
                r += 1 

            if r-l+1 > max_len:
                max_len = max(r-l +1, max_len) 
                res = s[l:r+1]

            l = mid 
            r = mid + 1 

            while l >= 0 and r <len(s) and s[l] == s[r]:
                l -= 1
                r += 1 
            
            if r-l+1 > max_len:
                max_len = max(r-l +1, max_len) 
                res = s[l:r+1]
        
        return res



class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) == 0 or len(s) == 1:
            return s 
        else:
            # initialization 
            max_len = 0
            res = ""

            for mid in range(len(s)): 
                # candidate palindrome이 홀수인 경우 
                l = r = mid 
                #res, max_len은 for loop을 돌면서 find_help func에 계속 들어가기 때문에 이름이 같아야함. (res, max_len)
                res, max_len = self.find_help(l, r, s, res, max_len)

                # candidate palindrome이 짝수인 경우: mid부터 for이 시작하니까 l이 mid가 되어야 함. 
                l, r = mid, mid+1
                res, max_len = self.find_help(l, r, s, res, max_len)
            return res
    
    def find_help(self, l, r, s, res, max_len) -> tuple:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # 크기먼저 비교하니까
            # 중간에서 시작해서 옆으로 커지면서 가장 큰 palindrome을 찾는다. 그러면 max len을 가외에서 찾아서 들어오는 것보다 확실하고 빠르게 찾을 수 있음. 
            #### 포인터를 옮기기 전에, max_len과 res를 저장해줘서 가장 작은 것부터 후에는 큰 것까지 모두 저장!! 
            if max_len < (r-l+1):
                res = s[l:r+1]
                max_len = r-l+1
            l -= 1 
            r += 1 
        return (res, max_len)


# 이 solution은 s가 길때 time limit이 뜸 
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) == 0 or len(s) == 1:
#             return s 
#         else:
#             # 처음과 끝 index 정하기 
#             # l은 0q부터, r은 1부터 시작 
#             max_len = 0
#             for l in range(0, len(s)):
#                 for r in range(l+1, len(s)+1):
#                     # 해당 처음과 끝이 palindrome인지 파악하기 
#                     new_s = s[l:r]
#                     if self.is_palindrome(new_s):
#                         # 길이 비교 해서 max_length와 max_result 에 저장하기
#                         if len(new_s) > max_len:
#                             max_len = len(new_s) 
#                             result = new_s
#         return result
                    
    
#     def is_palindrome(self, s: str) -> bool:
#         for i in range(len(s)):
#             if s[i] == s[-(i+1)]:
#                 continue
#             else:
#                 return False 
#         return True 

    
