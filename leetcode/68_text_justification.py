class Solution:
    # Total runtime: 74ms
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]

class MySolution:
    # Total runtime: 56ms
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        start = 0
        temp_len = 0
        while i < len(words):
            while i < len(words) and temp_len + len(words[i]) + 1 <= maxWidth+1:
                temp_len += len(words[i]) + 1
                i += 1
            temp_len -= 1
            lack_spaces = maxWidth - temp_len
            temp_words = words[start:i]
            for j in range(lack_spaces):
                temp_words[j % (len(temp_words)-1 or 1)] += ' '
            res.append(' '.join(temp_words))
            start = i
            temp_len = 0
        import re
        res[len(res) - 1] = re.sub(' +', ' ', res[len(res) - 1]).ljust(maxWidth)
        return res
            
            
            
            
            
