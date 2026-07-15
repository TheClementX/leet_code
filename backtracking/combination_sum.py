from typing import * 

def solution(candidates: list[int], target: int) -> list[list[int]]: 
    def get_combinations(cand, sum, comb, target): 
        if sum == target: return [list(comb)]
        if sum > target: return []

        result = []
        for i in range(len(cand)): 
            comb.append(cand[i])
            n_cand = cand[i:]
            new_combs = get_combinations(n_cand, sum+cand[i], comb, target)
            result.extend(new_combs)
            comb.pop()

        return result


    return get_combinations(candidates, 0, [], target)

"""
This is a more efficient solution because: 
    -> break early due to sorted ordering. 
    prevents loop from exploring unecessary paths
    -> uses an index to track list position instead of slicing
"""
def solution(candidates: list[int], target: int) -> list[list[int]]: 
    candidates = sorted(candidates)

    def get_combinations(cand, remaining, comb, idx): 
        if remaining == 0: 
            return [list(comb)]

        result = []
        for i in range(idx, len(cand)): 
            if cand[i] > remaining: break 
            comb.append(cand[i])
            combs = get_combinations(cand, remaining-cand[i], comb, i)
            result.extend(combs)
            comb.pop()

        return result

    return get_combinations(candidates, target, [], 0)



def test(solution): 
    candidates = [2,3,6,7]
    target = 7
    sol = solution(candidates, target)
    print(sol)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
