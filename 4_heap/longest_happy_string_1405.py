'''

input: 'a', 'b', 'c' 의 개수 a, b, c variable로 주어짐 
goal: happy한 string을 찾기 
output:happy한 string 반환 

string이 happy하려면 다음의 조건을 만족한다. 
1. 'a', 'b','c' 로만 이루어져 있음 
2. substring으로 'aaa', 'bbb', 'ccc'를 가지고 있지 않음 
    - substring: contiguous sequence of character 
3. input 에 들어온 대로 최대한 a, b, c occurance를 가진다. 


ex) 

a = 1, b= 1 , c= 7

output: 'ccaccbcc' 
'''

# Time:  O(n)
# Space: O(1)

import heapq


class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        max_heap = []
        if a:
            heapq.heappush(max_heap, (-a, 'a'))
        if b:
            heapq.heappush(max_heap, (-b, 'b'))
        if c:
            heapq.heappush(max_heap, (-c, 'c'))
        result = []
        
        # while문안에 pop 두개해서 res에 1번씩 더하고 다음번에는 앞앞것이 다를 경우에만 pop 한 것을 res에 더함. 
        # 앞앞 것이 같은데 더이상 heap안에 아무것도 없으면 res return 

        while max_heap:
            count1, c1 = heapq.heappop(max_heap)
            if len(result) >= 2 and result[-1] == result[-2] == c1:
                if not max_heap:
                    return "".join(result)
                count2, c2 = heapq.heappop(max_heap)
                result.append(c2) # result 
                count2 += 1
                if count2:
                    heapq.heappush(max_heap, (count2, c2))
                heapq.heappush(max_heap, (count1, c1))
                continue
            result.append(c1) # result 
            count1 += 1
            if count1 != 0:
                heapq.heappush(max_heap, (count1, c1))
        return "".join(result)