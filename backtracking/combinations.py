from typing import * 

def solution(n: int, k: int) -> list[list[int]]: 
    def get_combs(lo, hi, k, cur): 
        if k <= 0: return [cur]

        result = []
        for i in range(lo, hi+1): 
            next = cur + [i]
            result.extend(get_combs(i+1, hi, k-1, next))

        return result

    return get_combs(1, n, k, [])

def solution(n: int, k: int) -> list[list[int]]: 
    def get_combs(lo, hi, k, cur, result): 
        if k <= 0: 
            result.append(list(cur))
            return result

        for i in range(lo, hi-k+2): 
            cur.append(i)
            result = get_combs(i+1, hi, k-1, cur, result)
            cur.pop()

        return result

    return get_combs(1, n, k, [], [])



def test(solution): 
    sol = solution(4, 3)
    print(sol)
    sol = solution(6, 3)
    print(len(sol))
    print(sol)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
