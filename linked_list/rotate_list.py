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

def solution(head: Optional[ListNode], k: int) -> Optional[ListNode]: 
    if not head: return None

    len_list, cur_p = 0, head
    while cur_p: 
        len_list += 1
        cur_p = cur_p.next

    k %= len_list
    if len_list == 1 or k == 0: 
        return head

    split = len_list-k-1

    cur_p = head
    for _ in range(split): 
        cur_p = cur_p.next

    new_head = cur_p.next
    cur_p.next = None

    cur_p = new_head
    while cur_p.next: 
        cur_p = cur_p.next

    cur_p.next = head

    return new_head

def test(solution): 
    ll = array_to_ll([1,2,3,4,5])
    sol = ll_to_array(solution(ll, 3))
    print(sol)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
