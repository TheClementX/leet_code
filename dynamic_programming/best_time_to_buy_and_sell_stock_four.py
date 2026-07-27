from typing import * 

def solution(k: int, prices: list[int]) -> int: 
    if k >= len(prices) // 2: 
        profit = 0
        for i in range(1, len(prices)): 
            if prices[i] > prices[i-1]: 
                profit += prices[i] - prices[i-1]
        return profit

    buy = [float('-inf') for _ in range(k+1)] 
    sell = [0 for _ in range(k+1)]

    for price in prices: 
        for i in range(1, k+1): 
            print(buy, sell)
            buy[j] = max(buy[j], sell[j-1] - price)
            sell[j] = max(sell[j], buy[j] + price)

    return sell[k]

def test(solution): 
    prices = [2,4,1]
    sol = solution(2, prices)
    print(sol)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
