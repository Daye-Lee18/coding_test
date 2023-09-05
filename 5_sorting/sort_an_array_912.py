from typing import List 

'''
MergeSort 

'''
class Solution:
  def sortArray(self, nums: List[int]) -> List[int]:
    def mergeSort(A: List[int], l: int, r: int) -> None:
      if l >= r:
        return

      def merge(A: List[int], l: int, m: int, r: int) -> None:
        sorted = [0] * (r - l + 1)
        k = 0  # sorted's index
        i = l  # left's index
        j = m + 1  # right's index

        while i <= m and j <= r:
          if A[i] < A[j]:
            sorted[k] = A[i]
            k += 1
            i += 1
          else:
            sorted[k] = A[j]
            k += 1
            j += 1

        # Put the possible remaining left part into the sorted array.
        while i <= m:
          sorted[k] = A[i]
          k += 1
          i += 1

        # Put the possible remaining right part into the sorted array.
        while j <= r:
          sorted[k] = A[j]
          k += 1
          j += 1

        A[l:l + len(sorted)] = sorted

      m = (l + r) // 2
      mergeSort(A, l, m)
      mergeSort(A, m + 1, r)
      merge(A, l, m, r)

    mergeSort(nums, 0, len(nums) - 1)
    return nums

# QUICK SORT o(nlogn) o(n**2) at worst 
# input based recursion 


# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         self.quicksort(nums, 0, len(nums) - 1)
#         return nums
    
#     def quicksort(self, nums, lower, upper):
#         if lower < upper: # check if there is more than one element in the subarray 
#             pivot = self.partition(nums, lower, upper)
#             self.quicksort(nums, lower, pivot - 1)
#             self.quicksort(nums, pivot + 1, upper)
#         else:
#             return # there's no sorting to be done 
        
#     def partition(self, nums, lower, upper):
        
#         pivot = nums[upper] # choosing pivot, in this case the pivot starts from the last index 
        
#         # i is lower pointer 
#         i = lower
        
#         # j is upper pointer 
#         for j in range(lower, upper): 
#             if nums[j] < pivot: # if the element at j is less than pivot, swap nums[i] and nums[j] 
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i += 1 # i에는 후에 pivot의 위치랑 바꿀 것임. 
                
#         nums[i], nums[upper] = nums[upper], nums[i] # swaps the pivot element with the element at i to place the pivot in its correct position 
        
#         return i # 최종 pivot 의 위치 
