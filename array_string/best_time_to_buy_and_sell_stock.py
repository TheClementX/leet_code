from typing import * 

def solution(prices: List[int]) -> int: 
    """
    O(n) solution
    """
    mp = 0
    mv = prices[0]
    for i in range(1, len(prices)): 
        profit = prices[i] - mv
        if profit > mp: mp = profit
        if mv > prices[i]: mv = prices[i]

    return mp

def solution2(prices: List[int]) -> int: 
    """
    O(n^2) solution
    """
    mp = 0
    for i in range(len(prices)): 
        for j in range(i+1, len(prices)): 
            profit = prices[j] - prices[i]
            if profit > mp: mp = profit

    return mp


def test(solution: Callable[[List[int]], int]): 
    prices = [7,1,5,3,6,4]
    mp = solution(prices)
    print(mp)
    assert(mp == 5)

    prices = [30,60,1,2,3]
    mp = solution(prices)
    print(mp)
    assert(mp == 30)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
