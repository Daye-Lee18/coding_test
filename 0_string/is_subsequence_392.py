'''dynamic programming'''


# EX) s= "acb" , t= "ahbgdc", expected = false ( 순서를 지켜야함)
'''

input : string 2개 s, t 
목적: s 가 t의 subsequence이면 true 반환, 아니면 false 

s = "abc", t= "ahbhdc"  // output = true 

subsequence인 거는 그냥 s의 원소가 "앞에서부터 순서대로" t에 모두 있으면 됨. 

'''


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # Base Cases
        if not s:
            return True  # s is empty
        elif not t:
            return False  # t is empty
        # Recursive case
        # if first letters match, solve after first letters of s & t
        # else find s after first letter of t
        return self.isSubsequence(s[1:], t[1:]) if s[0] == t[0] else self.isSubsequence(s, t[1:])


'''내 풀이'''
# EX) s= "acb" , t= "ahbgdc", expected = false ( 순서를 지켜야함)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False 
    
        temp = ""
        for char in s:
            if char not in t:
                return False 
            else:
                temp += char
                try: 
                    ix = t.index(char)
    
                    if ix < len(t) -1: # ix가 마지막 ix가 아닐때 
                        t = t[ix+1:]
                        # print(t)
                    else:
                        break 
                except:
                    break
        

        if temp == s:
            return True 
        return False     