from typing import * 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution(head: Optional[ListNode]) -> bool: 
    if head == None: return False

    slow, fast = head, head.next
    while slow != None and fast != None: 
        if slow is fast: 
            return True
        else: 
            slow = slow.next
            fast = fast.next
            if fast != None: fast = fast.next

    return False

def solution(head: Optional[ListNode]) -> bool: 
    if head == None: return False

    slow, fast = head, head.next
    start = True
    while slow != None and fast != None: 
        if slow is fast and not first: 
            return True
        else: 
            slow = slow.next
            fast = fast.next
            if fast != None: fast = fast.next
        start = False

    return False

def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
