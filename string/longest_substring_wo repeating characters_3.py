class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # INIT 
        max_len = 0 
        len_s = len(s) 
        
        for l_idx, char in enumerate(s):
            r_idx = l_idx
            charSET= set()
            
            # charSET 에 현재 CHAR가 없을 때 NO repeating임 
            # 현재 idx에서 최대 길이의 without repeating 을 찾은 다음에 while 문 밖에서 if문으로 max_len을 update 해줌 
            # while안에서 if를 넣으면 너무 조잡하게 계산됨 
            while r_idx < len_s and s[r_idx] not in charSET:
                charSET.add(s[r_idx])
                r_idx += 1 
            if max_len < (r_idx - l_idx):
                max_len = r_idx - l_idx
        return max_len


'''
아래 방법은 s가 매우 긴 경우에 time limit이 뜸
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s == "":
            return 0 

        max_len = 0 
        # iterate char in s 
        for i in range(len(s)):
            for j in range(i+1, len(s) + 1):
                cur_s = s[i:j]
                # decide whether the cur_s is without repeating or not 
                if self.without_repeat(cur_s) and (j - i > max_len):
                    max_len = j-i
                    result = cur_s
        return max_len
    
    def without_repeat(self, s: str) -> bool:
        #INIT 
        char_dict = {}
        # print(ord('a'))
        # char가 ! 나 다른 기호일수도 있어서 안됨. 
        # for _ in range(ord('a'), ord('z')+1):
        #     char_dict[chr(_)] = 0 
        
        # char_dict[" "] = 0
        
        for char in s : 
            if char not in char_dict:
                char_dict[char] = 1 
            else: 
                return False 
        return True 