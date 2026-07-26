from typing import * 

def solution(coins: list[int], amount: int) -> int: 
    cache = [float('inf')] * (amount+1)
    cache[0] = 0

    for i in range(1, amount+1):
        for coin in coins: 
            if i - coin >= 0: 
                cache[i] = min(cache[i], cache[i - coin] + 1)
    
    return cache[amount] if cache[amount] != float('inf') else -1


def test(solution): 
    coins = [1,2,5]
    amount = 11
    sol = solution(coins, amount)
    print(sol)
    assert(sol == 3)

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
