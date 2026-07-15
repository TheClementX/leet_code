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

def solution(lists: list[Optional[ListNode]]) -> Optional[ListNode]: 
    if not lists: 
        return None

    def merge_two(left, right): 
        dummy = ListNode()
        cur_p = dummy

        while left and right: 
            if left.val < right.val: 
                cur_p.next = left
                left = left.next
            else:
                cur_p.next = right
                right = right.next
            cur_p = cur_p.next

        if left: cur_p.next = left
        if right: cur_p.next = right

        return dummy.next

    cur_lists, next_lists = lists, []
    while len(cur_lists) > 1: 
        while cur_lists: 
            if len(cur_lists) > 1: 
                l1 = cur_lists.pop()
                l2 = cur_lists.pop()
                next_lists.append(merge_two(l1, l2))
            else: 
                next_lists.append(cur_lists.pop())

        cur_lists = next_lists 
        next_lists = []

    return cur_lists[0]

def test(solution): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
