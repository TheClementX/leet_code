from typing import * 

def solution(digits: str) -> list[str]: 
    l_map = {
        "2": "abc", 
        "3": "def", 
        "4": "ghi", 
        "5": "jkl", 
        "6": "mno", 
        "7": "pqrs", 
        "8": "tuv", 
        "9": "wxyz"
    }

    def get_combinations(cur_word, digits): 
        if digits == "": return [cur_word]

        combinations = []
        n, next_digits = digits[0], digits[1:]

        for l in l_map[n]: 
            next_word = cur_word + l
            cur_combs = get_combinations(next_word, next_digits)
            combinations.extend(cur_combs)

        return combinations

    return get_combinations("", digits)

def test(solution): 
    digits = "245"
    sol = solution(digits)
    print(sol)

    digits = "23"
    sol = solution(digits)
    print(sol)

    digits = "2"
    sol = solution(digits)
    print(sol)


    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
