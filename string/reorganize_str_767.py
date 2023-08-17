import heapq
import collections 

class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s: return ""

        #create a counter 
        heap = []
        # store the letter and frequence as pair based on its frequence in max heap
        # key = the letter and value = frequence 
        for key, value in collections.Counter(s).iterms():
           heapq.heappush(heap, [-value, key])
        
        # res will be pre + curr 
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
