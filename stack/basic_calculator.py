from typing import * 
from math import *

def solution(s: str): 
    stack = []
    result = 0
    number = 0
    sign = 1

    for c in s: 
        if c.isdigit(): 
            number = number * 10 + int(c)
        elif c in '+-': 
            result += sign * number
            number = 0
            sign = 1 if c == '+' else -1
        elif c == '(': 
            stack.append(result)
            stack.append(sign)
            sign, result = 1, 0
        elif c == ')': 
            result += sign * number
            number = 0
            result *= stack.pop()
            result += stack.pop()

    result += sign * number

    return result

# def solution(s: str) -> int: 
#     def eval_rp(tokens: str) -> int: 
#         stack = []
#         for t in tokens: 
#             if t == '+' and len(stack) >= 2: 
#                 v1, v2 = stack.pop(), stack.pop()
#                 stack.append(v2 + v1)
#             elif t == '-' and len(stack) >= 2:
#                 v1, v2 = stack.pop(), stack.pop()
#                 stack.append(v2 - v1)
#             elif t == '*' and len(stack) >= 2:
#                 v1, v2 = stack.pop(), stack.pop()
#                 stack.append(v2 * v1)
#             elif t == '/' and len(stack) >= 2:
#                 v1, v2 = stack.pop(), stack.pop()
#                 stack.append(trunc(v2 / v1))
#             else: 
#                 stack.append(int(t))
# 
#         return stack[-1]
# 
#     def parse_string(s: str) -> List[str]: 
#         tokens = []
#         number, sign = 0, 1
#         for c in s: 
#             if c.isdigit(): 
#                 number = number * 10 + int(c)
#             elif c == '(' or c == ')': 
#                 tokens.append(str(sign * number))
#                 number, sign = 0, 1
#                 tokens.append(c)
#             elif c in '+-/*': 
#                 tokens.append(str(sign * number))
#                 if c == '-': 
#                     tokens.append('+')
#                     number, sign = 0, -1
#                 else:
#                     tokens.append(c)
#                     number, sign = 0, 1
# 
#         tokens.append(str(sign * number))
#         return tokens
# 
#     def shunting_yard(tokens): 
#         ops, out = [], []
#         def get_prec(t): 
#             match t: 
#                 case '+' | '-': return 0
#                 case '*' | '/': return 1
# 
#         for t in tokens: 
#             if t in '+-/*': 
#                 prec = get_prec(t)
#                 while ops and get_prec(ops[-1]) >= prec: 
#                     out.append(ops.pop())
#                 ops.append(t)
#             elif t == '(': 
#                 ops.append(t)
#             elif t == ')': 
#                 while ops and ops[-1] != '(': 
#                     out.append(ops.pop())
#                 ops.pop()
#             else:
#                 out.append(t)
# 
# 
# 
#     tokens = parse_string(s)
#     rp = shunting_yard(tokens)
#     return eval_rp(rp)

def test(solution: ): 
    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
