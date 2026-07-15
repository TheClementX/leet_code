from typing import * 

def solution(n: int) -> list[str]: 
    def match(p1, p2): 
        return p1 == '(' and p2 == ')'

    def generate(c, e, p_str, p_match, result): 
        if c >= e and p_match == []: 
            result.append("".join(p_str))
            return result
        elif c >= e: 
            return result

        p_strings = []
        for p in ['(', ')']: 
            if not p_match and p == ')': 
                continue

            if p_match and match(p_match[-1], p): 
                p_str.append(p)
                old_p = p_match.pop()
                generate(c+1, e, p_str, p_match, result)
                p_str.pop()
                p_match.append(old_p)
            else: 
                p_str.append(p)
                p_match.append(p)
                generate(c+1, e, p_str, p_match, result)
                p_str.pop()
                p_match.pop()

        return result

    return generate(0, 2*n, [], [], [])

def test(solution): 
    n = 1
    sol = solution(n)
    print(sol)

    n = 2
    sol = solution(n)
    print(sol)

    n = 3
    sol = solution(n)
    print(sol)
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
