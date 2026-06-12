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

def solution(head: Optional[ListNode], x: int) -> Optional[ListNode]: 
    if not head: return None
    leq, geq = ListNode(), ListNode()
    leq_p, geq_p = leq, geq

    cur_p = head
    while cur_p: 
        if cur_p.val < x: 
            leq_p.next = cur_p
            cur_p = cur_p.next
            leq_p = leq_p.next
            leq_p.next = None
        else:
            geq_p.next = cur_p
            cur_p = cur_p.next
            geq_p = geq_p.next
            geq_p.next = None
    
    leq_p.next = geq.next
    return leq.next

def test(solution): 
    ll = array_to_ll([1,5,2,4,3])
    sol = ll_to_array(solution(ll, 3))
    print(sol)
    assert(sol == [1,2,5,4,3])

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
