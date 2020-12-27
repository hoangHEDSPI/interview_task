from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digitsLength = len(digits)
        for i in range(digitsLength - 1, -1, -1):
            if (digits[i] < 9):
                digits[i] += 1
                return digits
            digits[i] = 0
        newDigits = [0 if i != 0 else 1  for i in range(digitsLength+1)]
        return newDigits

if __name__=="__main__":
    digits = [9]
    solution = Solution()
    print(solution.plusOne(digits))