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

def solution(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]: 
    if head == None: return None

    #iterate to 1 before reverse
    i, cur_p, pre = 1, head, None
    while i < left and cur_p != None: 
        pre = cur_p
        cur_p = cur_p.next
        i += 1

    rev_p, rev_tail = None, cur_p
    while i <= right and cur_p != None: 
        tmp = cur_p 
        cur_p = cur_p.next
        tmp.next = rev_p
        rev_p = tmp
        i += 1

    rev_tail.next = cur_p
    
    if pre: 
        pre.next = rev_p
        return head
    else: 
        return rev_p


def test(solution): 
    ll = array_to_ll([1,2,3,4,5])
    sol = solution(ll, 2, 4)
    print(ll_to_array(sol))
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
