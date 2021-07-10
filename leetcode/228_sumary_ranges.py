class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        
        res: List[str] = []
        start, i = 0, 0
        while i+1 < len(nums):
            if nums[i+1] != nums[i]+1:
                if start == i:
                    res.append(str(nums[i]))
                else:
                    res.append(str(nums[start]) + "->" + str(nums[i]))
                start = i+1
            i += 1
        if start == i:
            res.append(str(nums[start]))
        else:
            res.append(str(nums[start]) + "->" + str(nums[i]))
        return res
                
