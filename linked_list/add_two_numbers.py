from typing import * 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def array_to_ll(s: List[Any]) -> Optional[ListNode]: 
    if s == []: return None
    result = None
    for v in s: 
        result = ListNode(v, result)
    return result

def ll_to_array(head: Optional[ListNode]) -> None: 
    result = []
    while head != None: 
        result.append(head.val)
        head = head.next
    return result

def solution(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
    if l1 == None and l2 == None: return None

    r_h, result, r = None, None, 0
    while l1 != None and l2 != None: 
        sum = l1.val + l2.val + r
        val, r = sum % 10, sum // 10
        if r_h == None and result == None:
            result = ListNode(val, result)
            r_h = result
        else: 
            result.next = ListNode(val, None)
            result = result.next
        l1, l2 = l1.next, l2.next

    while l1 != None: 
        sum = l1.val + r
        val, r = sum % 10, sum // 10
        result.next = ListNode(val, None)
        result = result.next
        l1 = l1.next

    while l2 != None: 
        sum = l2.val + r
        val, r = sum % 10, sum // 10
        result.next = ListNode(val, None)
        result = result.next
        l2 = l2.next

    if r != 0: 
        result.next = ListNode(r, None)

    return r_h


def test(solution): 
    l1 = array_to_ll([2,4,3])
    l2 = array_to_ll([5,6,4])
    sol = ll_to_array(solution(l1, l2))
    print(sol)
    assert(sol == [7,0,8])


    l1 = array_to_ll([9,9,9,9,9,9,9])
    l2 = array_to_ll([9,9,9,9])
    sol = ll_to_array(solution(l1, l2))
    print(sol)
    assert(sol == [8,9,9,9,0,0,0,1])

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
