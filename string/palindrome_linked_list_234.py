# 풀이 1 
# - space complexity = O(N)
# - time complexity = O(N)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        # space complexity = O(N), time complexity = O(N)
        input_list = []
        cur = head 

        while cur:
            input_list.append(cur.val)
            cur = cur.next 
        # 중간 노드부터 시작 
        # 중간 노드 정의 // : 몫 
        
        mid = len(input_list)//2

        if len(input_list) == 0 or len(input_list) == 1:
            return True
        # 만약 짝수 linked list라면 
        elif len(input_list) % 2 == 0:
            l = mid - 1
            r = mid 
            # print(l, r)
        else:
            l = mid - 1
            r = mid + 1
            # print(l, r)
        while l >=0 and r < len(input_list):
            if input_list[l] == input_list[r]:
                l -= 1
                r += 1
            else:
                return False 
        return True
    
'''
# 풀이 2
- space complexity O(1) 
- time complexity O(N)

- runner algorithm 
  - reference: https://velog.io/@jayb/LeetCode-234.Palindrome-Linked-List%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC-%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8
  - linked list가 input으로 주어진 경우 runner 개념 (즉, 두 포인터의 속도차이를 내게 하여)을 사용하여 해당 문제는 palindrome이라 속도 차이가 2배 였는데 문제 상황에 따라 다른 속도도 가능할지 생각해볼 필요가 있음 

'''

class solution:
    def isPalindrome_2(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head 
        while fast and fast.next:
            fast = fast.next.next 
            rev, rev.next, slow = slow, rev, slow.next
        # 위의 while문에서 fast는 남아있고 fast.next가 없는 경우 = linked list의 길이가 홀수임
        # slow와 rev를 비교해야하므로 slow한칸 더 가야함.
        if fast:
            slow = slow.next 
        # palindrome 판별 
        while rev and rev.val == slow.val :
            slow, rev = slow.next , rev.next 
        # rev가 linked list의 맨 처음으로 간 경우는 none일것이므로 palindrome임
        return not rev 