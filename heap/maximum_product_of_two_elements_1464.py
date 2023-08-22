import heapq

# largest or smallest 나오면 heap을 생각하면 됨 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        heap = []

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                cur_product = (nums[i]-1) * (nums[j]-1)
                heapq.heappush(heap, -cur_product)
        
        return -heapq.heappop(heap)