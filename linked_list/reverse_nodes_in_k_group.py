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

    #get length
    len_list, cur_p = 0, head
    while cur_p != None: 
        len_list += 1
        cur_p = cur_p.next

    if len_lsit < k: 
        return head

    len_list -= len_list % k 
    
    #reverse independent portions
    reverses = []
    cur_p, rev_p = head, None
    i = 0
    while i < len_list and cur_p != None: 
        if i % k == 0 and i != 0: 
            reverses.append(rev_p)
            rev_p = None
        tmp = cur_p
        cur_p = cur_p.next
        tmp.next = rev_p 
        rev_p = tmp
        i += 1

    reverses.append(rev_p)
    reverses.append(cur_p)

    #concatenate
    for i in range(len(reverses)-1): 
        cur_h = reverses[i]
        while cur_h.next != None: 
            cur_h = cur_h.next
        cur_h.next = reverses[i+1]

    return reverses[0]

def test(solution): 
    ll = array_to_ll([1,2,1,2,1,2,1])
    sol = ll_to_array(solution(ll, k=2))
    print(sol)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
