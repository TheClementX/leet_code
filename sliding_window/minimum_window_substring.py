from typing import * 

def solution(s: str, t: str) -> str: 
    if s == t: return t

    best_window, best_len = "", len(s)+1 
    char_counts, char_set = dict(), set(t)
    for c in t: 
        char_counts[c] = char_counts.get(c, 0) + 1

    #sliding window logic
    lo, cur_counts = 0, dict()
    for hi in range(len(s)): 
        #increment counts iff c in char_set
        c = s[hi]
        if c in char_set: 
            cur_counts[c] = cur_counts.get(c, 0) + 1
            print(cur_counts, char_counts)

        while lo <= hi: 
            lo_c = s[lo]
            if lo_c not in char_set: 
                lo += 1 
            elif cur_counts[lo_c] > char_counts[lo_c]: 
                cur_counts[lo_c] -= 1
                lo += 1
            else: 
                break
            
        if cur_counts == char_counts and (hi-lo+1) < best_len: 
            best_window = s[lo:hi+1]
            best_len = hi-lo+1

    return best_window

def solution(s: str, t: str) -> str: 
    #edge cases
    if not s or not t or len(t) > len(s): 
        return "" 

    #count dictionaries
    char_count, cur_count = dict(), dict()
    for c in t: 
        char_count[c] = char_count.get(c, 0) + 1

    #have need counter for window guard
    have, need = 0, len(char_count.keys())
    best_len, window = len(s)+1, ""

    lo = 0
    for hi in range(len(s)): 
        c = s[hi]
        cur_count[c] = cur_count.get(c, 0) + 1
        if c in char_count and cur_count[c] == char_count[c]: 
            have += 1

        # shrinking logic based on have vs need
        while have == need: 
            if (hi-lo)+1 < best_len: 
                best_len = hi-lo+1
                window = s[lo:hi+1]

            lo_c = s[lo]
            cur_count[lo_c] -= 1
            
            if lo_c in char_count and cur_count[lo_c] < char_count[lo_c]: 
                have -= 1

            lo += 1 

    return window

def test(solution: Callable[[str, str], str]): 
    s = "ADOBECODEBANC"
    t = "ABC"
    sol = solution(s, t)
    print(sol)
    assert(sol == "BANC")

    s = "ab"
    t = "a"
    sol = solution(s, t)
    print(sol)
    assert(sol == "a")

    s = "aaaaaaaaaaaabbbbbcdd"
        #0123456789abcdefghij
    t = "abcdd"
    sol = solution(s, t)
    print(sol)
    assert(sol == "abbbbbcdd")

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
