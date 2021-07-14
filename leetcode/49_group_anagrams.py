class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = {}
        for word in strs:
            key = tuple(sorted(word))
            wordDict[key] = wordDict.get(key, []) + [word]
        return wordDict.values()
      
