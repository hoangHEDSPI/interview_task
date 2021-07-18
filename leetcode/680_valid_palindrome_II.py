class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Two pointers
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                # delete s[right]
                middleWithLeft = s[left:right]
                # delete s[left]
                middleWithRight = s[left+1:right+1]
                return middleWithLeft == middleWithLeft[::-1] or middleWithRight == middleWithRight[::-1]
            left, right = left+1, right-1
        return True
        
