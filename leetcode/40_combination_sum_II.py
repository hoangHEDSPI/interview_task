class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(combination, curr, remain, results):
            if remain == 0:
                results.append(list(combination))
                return
            for next_curr in range(curr, len(candidates)):
                if next_curr > curr and candidates[next_curr] == candidates[next_curr-1]:
                    continue
                picked = candidates[next_curr]
                if remain - picked < 0:
                    break
                combination.append(picked)
                backtrack(combination, next_curr+1, remain - picked, results)
                
                combination.pop()
        candidates.sort()
        comb, res = [], []
        backtrack(comb, 0, target, res)
        return res
      
