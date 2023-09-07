class Solution:
  def getPermutation(self, n: int, k: int) -> str:
    ans = ''
    nums = [i + 1 for i in range(n)]
    fact = [1] * (n + 1)  # fact[i] := i!

    for i in range(2, n + 1):
      fact[i] = fact[i - 1] * i

    k -= 1  # 0-indexed

    # j와 k는 k를 fact[i]로 나눈 각각 몫과 나머지 
    # j = 2 // fact[3] = 2 // 3! = 0
    # k = 2 % fact[3] = 2 % 3! = 6 
    # ans = nums[0] = '1'
    # nums = [2, 3]

    # j = 6 // fact[2] = 6 // 2! = 3 
    # k = 6%2! = 0 
    # ans = '13'
    # nums = [2] 



    for i in reversed(range(n)):
      j = k // fact[i]     # j is to find index of the numbe4r should be added to the resulat at the current position i 
      k %= fact[i]         # k is to be updated to keep track of the remaining permutations 
      ans += str(nums[j])
      nums.pop(j)          # make sure to remove the number from the nums list to ensure it's not used again in subsequent positions 
 
    return ans
