from typing import * 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def array_to_ll(s: List[Any]) -> Optional[ListNode]: 
    if s == []: return None
    result = None
    for i in range(len(s)-1, -1, -1): 
        result = ListNode(s[i], result)
    return result

def ll_to_array(head: Optional[ListNode]) -> None: 
    result = []
    while head != None: 
        result.append(head.val)
        head = head.next
    return result

def solution(head: Optional[ListNode]) -> Optional[ListNode]: 
    if not head: return None

    dummy = ListNode(next=head)
    prev = dummy
    cur_p = head
    while cur_p and cur_p.next:
        if cur_p.val == cur_p.next.val: 
            val = cur_p.val
            while cur_p != None and cur_p.val == val: 
                cur_p = cur_p.next
            prev.next = cur_p
        else: 
            prev = prev.next
            cur_p = cur_p.next

    return dummy.next
    
def test(solution): 
    ll = array_to_ll([1,1,2,3,4,4,5,5])
    sol = ll_to_array(solution(ll))
    print(sol)

    ll = array_to_ll([1])
    sol = ll_to_array(solution(ll))
    print(sol)

    ll = array_to_ll([1,1])
    sol = ll_to_array(solution(ll))
    print(sol)

    ll = array_to_ll([1,2,3,3,4,4,5])
    sol = ll_to_array(solution(ll))
    print(sol)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
