class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split(" ")
        res = " ".join([words[i] for i in range(k)])
        return res

if __name__ == '__main__':
    solution = Solution()
    s = "Hello how are you Contestant"
    k = 4
    assert solution.truncateSentence(s, k) == "Hello how are you"
