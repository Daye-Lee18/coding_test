'''
input: string s
goal: rearrange the characters of s so that any two adjacent characters are not the same 
output: rearranged string 

ex) 
s = "aab" 
output = "aba" 

s = "aaab" 
output = "" 

'''


import heapq
import collections 

class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s: return ""

        #create a counter 
        heap = []
        # store the letter and frequence as pair based on its frequence in max heap
        # key = the letter and value = frequence 
        # counter = dictionary form 
        # https://www.daleseo.com/python-heapq/ 
        # min heap이 기본이라, max heap을 해주려면 tuple을 원소로 추가하거나 삭제하면, 튜플내에서 맨 앞에 있는 값을 기준으로 min heap이 구성되는 원리를 이용한다. 
        # 인덱스 0은 우선순위이므로 나중에 값을 가져올 때는 index 1에 있는 값만 가져오면 된다. 
        for key, value in collections.Counter(s).items():
           heapq.heappush(heap, [-value, key])
        
        # res will be pre + curr 
        # if s = "aab", res = 'a' + 'b' + 
        res = ""
        pre = heapq.heappop(heap)
        res += pre[1]

        while heap:
            curr = heapq.heappop(heap)
            res += curr[1] 

            pre[0] += 1 # max heap을 이용했으므로 +1 를 해줘야 0에 가까워짐 
            
            # 아직 횟수가 남았으므로 heap에 다시 넣어줌 
            if pre[0] <0:
                heapq.heappush(heap, pre)
            
            pre = curr 

        return "" if len(res) != len(s) else res 
    

if __name__ == '__main__':
    s = "aaabbcd"
    x = Solution()
    print(x.reorganizeString(s)) # babacd 
    
