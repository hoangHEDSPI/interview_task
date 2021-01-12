from typing import List
class Solution:
    @staticmethod
    def backtrack(result_list: List[List[int]], temp_list: List[int], candidates: List[int], remain, start):
        if remain < 0:
            return
        if remain == 0:
            result_list.append(temp_list)
        else:
            for i in range(start, len(candidates)):
                temp_list.append(candidates[i])
                Solution.backtrack(result_list, temp_list, candidates, remain-candidates[i], i)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result_list: List[List[int]] = []
        temp_list = []
        candidates.sort() 
        Solution.backtrack(result_list, temp_list, candidates, target, 0)
        return result_list

if __name__=="__main__":
    sol = Solution()
    candidates = [2,3,6,7], target = 7
    sol.combinationSum(candidates, target)


