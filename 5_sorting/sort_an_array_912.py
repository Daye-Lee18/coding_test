from typing import List 

# QUICK SORT o(nlogn) o(n**2) at worst 
# input based recursion 
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums
    
    def quicksort(self, nums, lower, upper):
        if lower < upper: # check if there is more than one element in the subarray 
            pivot = self.partition(nums, lower, upper)
            self.quicksort(nums, lower, pivot - 1)
            self.quicksort(nums, pivot + 1, upper)
        else:
            return # there's no sorting to be done 
        
    def partition(self, nums, lower, upper):
        
        pivot = nums[upper] # choosing pivot, in this case the pivot starts from the last index 
        
        # i is lower pointer 
        i = lower
        
        # j is upper pointer 
        for j in range(lower, upper): 
            if nums[j] < pivot: # if the element at j is less than pivot, swap nums[i] and nums[j] 
                nums[i], nums[j] = nums[j], nums[i]
                i += 1 # i에는 후에 pivot의 위치랑 바꿀 것임. 
                
        nums[i], nums[upper] = nums[upper], nums[i] # swaps the pivot element with the element at i to place the pivot in its correct position 
        
        return i # 최종 pivot 의 위치 


'''
MergeSort 

'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i , j, k = L, 0, 0

            while j < len(left) and k < len(right): # only one of them is run out of, it will stop 
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = left[j]
                    k += 1
                i += 1 

            # if left subarray still left 
            while j < len(left):
                nums[i] = left[j]
                j += 1 
                i += 1 
            # if the right subarray stil have value 
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1 

        def mergeSort(arr, l, r):
            if l == r:
                return arr 
            
            m = (l+r) //2 
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)
            return arr 
    
        return mergeSort(nums, 0, len(nums)-1)
