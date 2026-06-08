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

    result, cur_p = None, head
    while cur_p != None: 
        tmp = cur_p 
        cur_p = cur_p.next
        tmp.next = result
        result = tmp

    return result


def test(solution): 
    ll = array_to_ll([1,2,3,4,5])
    sol = ll_to_array(solution(ll))
    print(sol)
    assert(sol == [5,4,3,2,1])

    ll = array_to_ll([5])
    sol = ll_to_array(solution(ll))
    print(sol)
    assert(sol == [5])

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
