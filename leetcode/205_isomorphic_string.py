class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sDict = {}
        tDict = {}
        for i in range(len(s)):
            if s[i] not in sDict:
                sDict[s[i]] = i
            else:
                if t[sDict[s[i]]] != t[i]:
                    return False
            if t[i] not in tDict:
                tDict[t[i]] = i
            else:
                if s[tDict[t[i]]] != s[i]:
                    return False     
        return True
  
