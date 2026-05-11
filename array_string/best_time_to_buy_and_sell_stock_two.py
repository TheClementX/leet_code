from typing import * 

def solution(prices: List[int]) -> int: 
    tot_p, max_p = 0, 0
    mv = prices[0]

    for i in range(1, len(prices)): 
        profit = prices[i] - mv
        if profit > max_p: max_p = profit
        if prices[i] < prices[i-1]: 
            tot_p += max_p
            max_p = 0
            mv = prices[i]

    return tot_p + max_p

def test(solution: Callable[[List[int]], int]): 
    prices = [7,1,5,3,6,4]
    mp = solution(prices)
    print(mp)
    assert(mp == 7)

    prices = [30,60,1,2,3]
    mp = solution(prices)
    print(mp)
    assert(mp == 32)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
