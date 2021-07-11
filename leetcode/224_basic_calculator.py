class Solution:
    def calculate(self, s: str) -> int:
        # default sign value is +1 (sign can either be +1 or -1)
        # num will store the current considering number
        # res will store the result
        
        num, sign, res = 0, 1, 0
        stack = []
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c in '+-':
                res += num*sign
                sign = -1 if c == '-' else 1
                num = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res += sign*num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num*sign
    
