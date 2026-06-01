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

def solution(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
    if not list1 and not list2: return None

    dummy = ListNode()
    cur = dummy
    while list1 != None and list2 != None: 
        if list1.val <= list2.val: 
            cur.next = list1
            list1 = list1.next
        else: 
            cur.next = list2
            list2 = list2.next
        cur = cur.next


    if list2 != None: cur.next = list2
    if list1 != None: cur.next = list1

    return dummy.next

def test(solution): 
    l1 = array_to_ll([1,2,4])
    print(ll_to_array(l1))
    l2 = array_to_ll([1,3,4])
    print(ll_to_array(l2))
    sol = ll_to_array(solution(l1, l2))
    print(sol)
    assert(sol == [1,1,2,3,4,4])

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
