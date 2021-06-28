class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN = -2**31
        MAX = 2**31 - 1
        res = dividend/divisor
        rounded_res = dividend//divisor
        if res != rounded_res and rounded_res < 0:
            rounded_res += 1
        
        if rounded_res < MIN:
            rounded_res = MIN
        elif rounded_res > MAX:
            rounded_res = MAX
        return rounded_res
      
