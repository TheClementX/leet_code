from typing import * 

def solution(prices: list[int]): 
    if not prices: return 0

    forward = [0] * len(prices)
    backward = [0] * len(prices)

    #forward pass 
    cur_min = prices[0]
    for i in range(1, len(prices)): 
        cur_min = min(cur_min, prices[i])
        forward[i] = max(forward[i-1], prices[i]-cur_min)

    #backward pass
    cur_max = prices[len(prices)-1]
    for i in range(len(prices)-2, -1, -1): 
        cur_max = max(cur_max, prices[i])
        backward[i] = max(backward[i+1], cur_max-prices[i])

    max_total = 0
    for i in range(len(prices)): 
        max_total = max(max_total, backward[i] + forward[i])

    return max_total

def test(solution): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
