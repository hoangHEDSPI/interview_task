class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = abs(x)
        y = str(y)
        y = y[::-1]
        if x < 0:
            y = -int(y)
        else:
            y = int(y)
        if (y < pow(-2, 31) or y > pow(2,31)-1):
            return 0
        else:
            return y
        
