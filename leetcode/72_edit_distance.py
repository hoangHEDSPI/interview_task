class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """DP bottom-up approach."""
        if word1 is None or word2 is None:
            return -1
        len_word1 = len(word1)
        len_word2 = len(word2)
        if len_word1 == 0 and len_word2 != 0:
            return len_word2
        if len_word1 != 0 and len_word2 == 0:
            return len_word1
        matched = [[0 for _ in  range(len_word1+1)] for _ in range(len_word2+1)]
        for i in range(len_word2):
            matched[i][0] = i
        for j in range(len_word1):
            matched[0][j] = j
        for i in range(len_word2):
            for j in range(len_word1):
                if word2[i] == word1[j]:
                    matched[i+1][j+1] = matched[i][j]
                else:
                    matched[i+1][j+1] = min(matched[i][j+1], matched[i+1][j], matched[i][j]) + 1
        
        return matched[len_word2][len_word1]

if __name__=='__main__':
    sol = Solution()
    word1 = 'distance'
    word2 = 'springbok'
    print(sol.minDistance(word1, word2))
