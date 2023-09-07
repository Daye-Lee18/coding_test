
'''
input = string s 
output = the length of longest palindrome 

ex) 

s = 'abcccdd'
output = 7 <- 'dccaccd' 

s = 'a'
output = 1 <- 'a' 

'''

from collections import Counter 

class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s) 

        max_len = 0 
        is_odd = False 
        print(cnt)
        for key, value in cnt.items():
            max_len += (value // 2) * 2 
            cnt[key] = value % 2 

            if is_odd == False and max_len % 2 == 0 and cnt[key] == 1 : # value값은 위에서 update될 수도 있어서 cnt[key]로 condition 비교해야함 
                max_len += 1 
                is_odd = True # 딱 한번만 진행 
        return max_len
        

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