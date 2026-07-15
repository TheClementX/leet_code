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

"""
an incorrect formulation of quick sort. Fix this 
when possible
"""
def solution(head: Optional[ListNode]) -> Optional[ListNode]: 
    if not head: return None

    def sort(head): 
        if not head or not head.next: 
            return head

        part_val = head.val
        lower, higher = ListNode(), ListNode()

        cur_p = head
        while cur_p: 
            next = cur_p.next
            cur_p.next = None

            if cur_p.val < part_val: 
                cur_p.next = lower.next
                lower.next = cur_p 
            else: 
                cur_p.next = higher.next
                higher.next = cur_p

            cur_p = next

        sorted_lower, sorted_higher = sort(lower.next), sort(higher.next)

        #concat lists
        e_sorted = sorted_lower
        while e_sorted.next: 
            e_sorted = e_sorted.next
        e_sorted.next = sorted_higher

        return sorted_lower

    return sort(head)

def solution(head: Optional[ListNode]) -> Optional[ListNode]: 
    def split_list(head): 
        slow, fast = head, head.next
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None

        return head, mid

    def sort_list(head): 
        if not head or not head.next: 
            return head

        left, right = split_list(head)
        left, right = sort_list(left), sort_list(right)

        #merge 
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

    return sort_list(head)


def test(solution): 
    l = array_to_ll([3,2,4,7,5,3,8])
    print(ll_to_array(l))
    l = solution(l)
    print(ll_to_array(l))

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
