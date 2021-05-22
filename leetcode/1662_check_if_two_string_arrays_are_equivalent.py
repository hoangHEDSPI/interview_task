from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        sorted(word1)
        sorted(word2)
        return "".join([word for word in word1]) == "".join([word for word in word2])

if __name__ == '__main__':
    solution = Solution()
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    assert solution.arrayStringsAreEqual(word1, word2) == True
    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    assert solution.arrayStringsAreEqual(word1, word2) == False
    word1  = ["abc", "d", "defg"]
    word2 = ["abcddefg"]
    assert solution.arrayStringsAreEqual(word1, word2) == True
