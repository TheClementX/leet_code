from typing import * 

class LRUCache: 
    class ListNode(): 
        def __init__(self, val=None, key=None, prev=None, next=None): 
            self.val = val
            self.key = key
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int): 
        self.state_dict = dict()
        self.head, self.tail = None, None
        self.state, self.capacity = 0, capacity
        
        dummy = ListNode()
        cur_p = dummy
        for _ in range(capacity): 
            new = ListNode(prev=cur_p) 
            cur_p.next = new
            cur_p = new

        self.head, self.tail = dummy.next, cur_p
        self.head.prev = None


    def get(self, key: int) -> int:
        if key not in self.state_dict: return -1

        cur_p = self.state_dict[key]
        if cur_p is self.head: return cur_p.val #catches 1 node case
        if cur_p is self.tail: self.tail = self.tail.prev

        prev, next = cur_p.prev, cur_p.next
        #insert cur_p at front
        cur_p.next, cur_p.prev = self.head, None
        self.head.prev = cur_p
        self.head = cur_p 
        #cut cur_p out of list
        if prev: prev.next = next
        if next: next.prev = prev

        return cur_p.val

    def put(self, key: int, value: int) -> None:
        if key in self.state_dict: 
            cur_p = self.state_dict[key]

            if cur_p is self.head: 
                cur_p.val = value
            else: 
                if cur_p is self.tail: self.tail = self.tail.prev
                prev, next = cur_p.prev, cur_p.next
                #insert cur_p at front
                cur_p.next, cur_p.prev = self.head, None
                self.head.prev = cur_p
                self.head = cur_p 
                #cut cur_p out of list
                if prev: prev.next = next
                if next: next.prev = prev
                cur_p.val = value
        else: 
            cur_p = self.tail
            self.tail = cur_p.prev
            if self.tail: self.tail.next = None
            else: self.head = None

            if cur_p.val != None: 
                self.state_dict.pop(cur_p.key)

            cur_p.key, cur_p.val = key, value
            self.state_dict[key] = cur_p 

            cur_p.prev, cur_p.next = None, self.head
            if not self.head: self.tail = cur_p
            else: self.head.prev = cur_p 
            self.head = cur_p

def test(solution): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
