class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import defaultdict
        from collections import deque
        # Corner cases 
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        
        commonLen = len(beginWord)
        
        allCombinationDict = defaultdict(list)
        for word in wordList:
            for i in range(commonLen):
                allCombinationDict[word[:i] + "*" + word[i+1:]].append(word)
        
        queue = deque([(beginWord, 1)])
        visited = {beginWord: True}
        
        while queue:
            currentWord, level = queue.popleft()
            for i in range(commonLen):
                intermediateWord = currentWord[:i] + '*' + currentWord[i+1:]
                for word in allCombinationDict[intermediateWord]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level+1))
                allCombinationDict[intermediateWord] = []
        return 0
      
