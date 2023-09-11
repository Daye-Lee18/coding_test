
from _LinkedList_helper import ListNode, create_linked_list, print_linked_list

# linked list는 dummy를 항상 생각한다. 

def P4(num1: ListNode, num2: ListNode) -> ListNode:    
    def fn(node): 
        """Reverse a linked list."""
        prev = None
        while node: 
            prev, node.next, node = node, prev, node.next
        return prev 
    
    num1, num2 = fn(num1), fn(num2) # reverse num1 & num2
    carry = 0
    dummy = node = ListNode()
    while carry or num1 or num2:
        if num1: 
            carry += num1.val
            num1 = num1.next
        if num2: 
            carry += num2.val
            num2 = num2.next
        carry, x = divmod(carry, 10) # 몫 & 나머지
        node.next = node = ListNode(x) # 다음에 연산되는 x가 지금 노드의 옆에 붙도록 노드 위치를 오른쪽으로 옮겨줌
        # 위의 코드를 두 줄 / 세 줄 로 나눠쓰면,
            # new_node = ListNode(x)
            # node.next = new_node
            # node = new_node # node = node.next를 한 것과 동일한 결과임 ,위에서 node.next가 new_node를 가리키므로 
        

            # node.next = ListNode(x)
            # node = node.next

            ###### ''' 이 아래 건 안됨'''
            # node.next = ListNode(x)
            # node = ListNode(x)

    return fn(dummy.next) # dummy.next 하는 이유: 항상 지금 구한 노드 값을 바로 오른쪽으로 넘겨 주기 때문에 마지막 node 값은 비어있을 것


if __name__ == '__main__':
    x = create_linked_list([1,2,3])
    y =  create_linked_list([8,1,7])
    z = P4(x, y)
    print_linked_list(z, []) 