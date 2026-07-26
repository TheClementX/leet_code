from typing import * 
import heapq

class MedianFinder: 
    def __init__(self): 
        self.l_heap = [] #max heap
        self.ge_heap = [] #min heap
        self.elements = 0
        self.median = None

    def balance_heaps(self): 
        while (len(self.ge_heap) > 1 + len(self.l_heap) or
               len(self.ge_heap) < len(self.l_heap)): 
            if len(self.ge_heap) > len(self.l_heap): 
                ge_top = heapq.heappop(self.ge_heap)
                heapq.heappush(self.l_heap, -1*ge_top)
            else: 
                l_top = heapq.heappop(self.l_heap)
                heapq.heappush(self.ge_heap, -1*l_top)

    def addNum(self, num: int) -> None: 
        if (not self.ge_heap 
            or num >= self.ge_heap[0]): 
            heapq.heappush(self.ge_heap, num)
        else: 
            heapq.heappush(self.l_heap, -1*num)
        self.elements += 1

        self.balance_heaps()
        self.update_median()

    def update_median(self): 
        if self.elements % 2 == 0: 
            self.median = (self.ge_heap[0] + (-1*self.l_heap[0])) / 2
        else: 
            self.median = float(self.ge_heap[0])

    def findMedian(self) -> float: 
        if self.median is not None: 
            return self.median

def test(): 
    median = MedianFinder()
    for i in range(10): 
        median.addNum(i)
    print(median.findMedian())

    median = MedianFinder()
    for n in [0,0]: 
        median.addNum(n)
    print(median.findMedian())

    median = MedianFinder()
    for n in [-1,-2,-3,-4,-5]: 
        median.addNum(n)
    print(median.findMedian())

    median = MedianFinder()
    for n in [1,2,3]: 
        median.addNum(n)
        print(median.ge_heap)
        print(median.l_heap)
        print(median.findMedian())


if __name__ == "__main__": 
    test() 


    
