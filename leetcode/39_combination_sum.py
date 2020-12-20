from typing import List


class Solution:
    # This solution has a bug and is under fixing
    @staticmethod
    def backtrack(result_list: List[List[int]], temp_list: List[int], candidates: List[int], remain, start):
        print(result_list)
        if remain == 0:
            result_list.append(temp_list)
            return
        else:
            for i in range(start, len(candidates)):
                if (candidates[i] > remain):
                    break
                temp_list.append(candidates[i])
                Solution.backtrack(result_list, temp_list, candidates, remain-candidates[i], i)
                temp_list.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result_list = []
        Solution.backtrack(result_list, [], candidates, target, 0)
        return result_list

class Solution2(object):
    # This is a solution from leetcode's member with the same ideal with mine
    # and somehow this solution worked
    def combinationSum(self, candidates, target):
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret
    
    def dfs(self, nums, target, path, ret):
        if target < 0:
            return 
        if target == 0:
            ret.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)

if __name__=="__main__":
    candidates: List[int]= [2,3,6,7]
    target = 7
    solution = Solution()
    result_list = solution.combinationSum(candidates, target)
