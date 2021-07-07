class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        from collections import Counter
        counter = Counter(arr).most_common()
        duplicated_nums = 0
        i = 0
        
        while duplicated_nums < len(arr) / 2:
            duplicated_nums += counter[i][1]
            i += 1
        return i
      
