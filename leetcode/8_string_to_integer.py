class Solution:
    def myAtoi(self, s: str) -> int:
        MIN = (-2)**31
        MAX = 2**31 - 1
        res = ''
        
        # Remove all leading whitespsace
        s = s.lstrip()
        num = ''
        is_negative = False
        
        i = 0
        while i < len(s):
            if i == 0 and s[i] == '-':
                is_negative = True
                i += 1
            elif i == 0 and s[i] == '+':
                i += 1
            elif s[i].isdigit():
                num += s[i]
                i += 1
            else:
                break
        if len(num) > 0:
            num = int(num)
            if is_negative:
                num = 0 - num
            if num < MIN:
                num = MIN
            if num > MAX:
                num = MAX
            return num
        return 0
      
