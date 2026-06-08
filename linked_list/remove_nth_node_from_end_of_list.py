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

def solution(head: Optional[ListNode], n: int) -> Optional[ListNode]: 
    if not head: return None
        
    #get length 
    cur_p, len_list = head, 0
    while cur_p != None: 
        len_list += 1
        cur_p = cur_p.next

    if n > len_list: return head

    t_idx = len_list-n
    dummy = ListNode(next=head)
    i, cur_p = 0, dummy
    while cur_p.next != None: 
        if i == t_idx: 
            tmp = cur_p.next
            cur_p.next = tmp.next
        cur_p = cur_p.next
        if not cur_p: break
        i += 1

    return dummy.next

def solution2(): 
    """
    single pass solution
    """
    pass
        

def test(solution): 
    ll = array_to_ll([1,2,3,4,5])
    sol = ll_to_array(solution(ll, 2))
    print(sol)

    ll = array_to_ll([1,2])
    sol = ll_to_array(solution(ll, 1))
    print(sol)

    ll = array_to_ll([1,2])
    sol = ll_to_array(solution(ll, 2))
    print(sol)

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
