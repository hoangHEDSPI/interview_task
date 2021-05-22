class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        result = ["" for _ in range(len(words))]
        for word in words:
            word_position = int(word[-1])
            result[word_position-1] = word[:-1]
        result = " ".join([word for word in result])
        return result

if __name__ == '__main__':
    solution = Solution()
    s = "is2 sentence4 This1 a3"
    assert solution.sortSentence(s) == "This is a sentence"