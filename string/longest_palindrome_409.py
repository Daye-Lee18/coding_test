
class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        len_s = len(s)
        max_len = 0 

        if len_s == 0:
            return 0
        if len_s == 1 :
            return 1 
        for i in range(len_s):
            # if the length of candidate palindromic substrig is even 
            l = i 
            r = l + 1 
            while l >= 0 and r < len_s:
                if s[l] == s[r]:
                    if max_len < r-l+1:
                        max_len = r-l+1    
                    l -= 1 
                    r += 1
                else:
                    break 

            
            
            # if the length of candidate palindromic substrig is odd 
            l = r = i  
            while l >= 0 and r < len_s:
                if s[l] == s[r]:
                    # sub_pal = s[l:r+1]
                    if max_len < r-l+1:
                        max_len = r-l+1
                    l -= 1 
                    r += 1
                else:
                    break 

        return max_len 

            
