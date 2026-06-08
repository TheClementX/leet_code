from typing import * 

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

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

def solution(head: Optional[Node]) -> Optional[Node]: 
    if head == None: return None

    dummy = Node(0)
    cur = dummy 
    orig_rands = []
    cur_p = head
    while cur_p != None: 
        cur.next = Node(cur_p.val, None, cur_p.random)
        orig_rands.append(cur_p.random)
        cur_p.random = cur.next
        cur_p = cur_p.next
        cur = cur.next

    cur = dummy.next
    while cur != None:
        if cur.random != None: 
            cur.random = cur.random.random
        cur = cur.next

    cur_p = head
    i = 0
    while cur_p != None: 
        cur_p.random = orig_rands[i]
        cur_p = cur_p.next
        i += 1

    return dummy.next

def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
