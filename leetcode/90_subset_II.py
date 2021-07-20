class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(nums: List[int], subsets: List[List[int]], currentSubset: List[int]):
            subsets.append(currentSubset)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                helper(nums[i+1:], subsets, currentSubset + [nums[i]])
        subsets = []
        helper(sorted(nums), subsets, [])
        return subsets
